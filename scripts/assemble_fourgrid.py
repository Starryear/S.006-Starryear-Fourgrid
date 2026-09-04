#!/usr/bin/env python3
"""Assemble four panels and a transparent subject-line junction into a 2×2 master."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble source, poetic, structure, and soul panels into a 2:3 2×2 artwork."
    )
    parser.add_argument("source", type=Path, help="Original source photograph")
    parser.add_argument("poetic", type=Path, help="Panel 2: poetic distillation")
    parser.add_argument("structure", type=Path, help="Panel 3: rhythmic structure")
    parser.add_argument("soul", type=Path, help="Panel 4: abstract soul")
    parser.add_argument("output", type=Path, help="Output PNG or JPEG path")
    parser.add_argument("--width", type=int, default=3072, help="Master width; default 3072")
    parser.add_argument("--height", type=int, default=4608, help="Master height; default 4608")
    parser.add_argument("--gutter", type=int, default=4, help="Internal divider width; default 4")
    parser.add_argument(
        "--fill", required=True,
        help="Source-derived divider and source-contain fill color, such as #DCE5E8",
    )
    parser.add_argument(
        "--source-mode", choices=("crop", "contain"), default="contain",
        help="Fit source by cropping or padding; generated panels are always cropped",
    )
    parser.add_argument(
        "--bridge", type=Path, required=True,
        help="Transparent PNG carrying the source-derived central junction motif",
    )
    parser.add_argument(
        "--bridge-scale", type=float, default=0.16,
        help="Bridge width as a fraction of master width; default 0.16",
    )
    parser.add_argument(
        "--bridge-x", type=float, default=0.50,
        help="Normalized horizontal center of bridge; default 0.50",
    )
    parser.add_argument(
        "--bridge-y", type=float, default=0.50,
        help="Normalized vertical center of bridge; default 0.50",
    )
    parser.add_argument(
        "--bridge-opacity", type=float, default=1.0,
        help="Bridge opacity from 0 to 1; default 1",
    )
    return parser.parse_args()


def open_rgb(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGB")


def open_bridge(path: Path) -> Image.Image:
    with Image.open(path) as image:
        bridge = ImageOps.exif_transpose(image).convert("RGBA")
    alpha = bridge.getchannel("A")
    alpha_min, alpha_max = alpha.getextrema()
    if alpha_max == 0:
        raise SystemExit("bridge image is fully transparent")
    if alpha_min > 0:
        raise SystemExit("bridge must contain fully transparent background pixels")
    bbox = alpha.getbbox()
    if bbox is None:
        raise SystemExit("bridge has no visible content")
    return bridge.crop(bbox)


def fit_panel(image: Image.Image, size: tuple[int, int], *, contain: bool, fill: str) -> Image.Image:
    if contain:
        return ImageOps.pad(image, size, color=ImageColor.getrgb(fill), method=Image.Resampling.LANCZOS)
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def add_bridge(master: Image.Image, bridge: Image.Image, args: argparse.Namespace) -> Image.Image:
    target_w = max(1, round(master.width * args.bridge_scale))
    target_h = max(1, round(bridge.height * target_w / bridge.width))
    max_h = max(1, round(master.height * 0.22))
    if target_h > max_h:
        target_h = max_h
        target_w = max(1, round(bridge.width * target_h / bridge.height))
    bridge = bridge.resize((target_w, target_h), Image.Resampling.LANCZOS)

    if args.bridge_opacity < 1:
        alpha = bridge.getchannel("A").point(lambda value: round(value * args.bridge_opacity))
        bridge.putalpha(alpha)

    left = round(master.width * args.bridge_x - bridge.width / 2)
    top = round(master.height * args.bridge_y - bridge.height / 2)
    left = max(0, min(master.width - bridge.width, left))
    top = max(0, min(master.height - bridge.height, top))
    overlay = Image.new("RGBA", master.size, (0, 0, 0, 0))
    overlay.alpha_composite(bridge, dest=(left, top))
    return Image.alpha_composite(master.convert("RGBA"), overlay).convert("RGB")


def main() -> None:
    args = parse_args()
    if args.width <= 0 or args.height <= 0 or args.gutter < 0:
        raise SystemExit("width and height must be positive; gutter cannot be negative")
    if not 0 < args.bridge_scale <= 0.40:
        raise SystemExit("bridge-scale must be greater than 0 and no more than 0.40")
    if not 0 <= args.bridge_x <= 1 or not 0 <= args.bridge_y <= 1:
        raise SystemExit("bridge-x and bridge-y must be between 0 and 1")
    if not 0 < args.bridge_opacity <= 1:
        raise SystemExit("bridge-opacity must be greater than 0 and no more than 1")
    if args.width * 3 != args.height * 2:
        raise SystemExit("master canvas must have an exact 2:3 aspect ratio")

    if args.width % 2 or args.height % 2:
        raise SystemExit("width and height must both be even")
    panel_w = args.width // 2
    panel_h = args.height // 2
    if panel_w * 3 != panel_h * 2:
        raise SystemExit("each quadrant must have an exact 2:3 aspect ratio")
    if args.gutter >= min(panel_w, panel_h):
        raise SystemExit("gutter must be smaller than a quadrant")

    source = fit_panel(
        open_rgb(args.source), (panel_w, panel_h),
        contain=args.source_mode == "contain", fill=args.fill,
    )
    generated = [
        fit_panel(open_rgb(path), (panel_w, panel_h), contain=False, fill=args.fill)
        for path in (args.poetic, args.structure, args.soul)
    ]

    master = Image.new("RGB", (args.width, args.height), ImageColor.getrgb(args.fill))
    positions = (
        (0, 0),
        (panel_w, 0),
        (0, panel_h),
        (panel_w, panel_h),
    )
    for panel, position in zip((source, *generated), positions):
        master.paste(panel, position)

    if args.gutter:
        divider = ImageColor.getrgb(args.fill)
        half = args.gutter // 2
        draw = ImageDraw.Draw(master)
        draw.rectangle((panel_w - half, 0, panel_w - half + args.gutter - 1, args.height - 1), fill=divider)
        draw.rectangle((0, panel_h - half, args.width - 1, panel_h - half + args.gutter - 1), fill=divider)

    master = add_bridge(master, open_bridge(args.bridge), args)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    suffix = args.output.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        master.save(args.output, quality=98, subsampling=0)
    elif suffix == ".png":
        master.save(args.output, optimize=True)
    else:
        raise SystemExit("output must end in .png, .jpg, or .jpeg")


if __name__ == "__main__":
    main()
