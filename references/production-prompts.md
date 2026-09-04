# Production prompt builder

Use after completing `source-analysis.md`. Replace every bracketed field with source-specific facts. Never send brackets or generic example content to the image tool.

## Shared prompt block

Include this logic in all generated panels:

```text
Use the supplied photograph as the sole content, structure, color, light, and emotional reference.

Source facts:
- primary subject and protected evidence: [PRIMARY_SUBJECT_AND_PROTECTED_EVIDENCE]
- identity contour and principal subject line: [IDENTITY_CONTOUR_AND_LINE]
- dominant axis and movement: [AXIS_AND_MOVEMENT]
- count, rhythm, and density map: [COUNT_RHYTHM_DENSITY]
- negative-space shape: [NEGATIVE_SPACE]
- source palette roles: dominant [DOMINANT], dark structural [DARK], light [LIGHT], secondary [SECONDARY], scarce accent [ACCENT]
- warm/cool balance and light direction: [TEMPERATURE_AND_LIGHT]
- SOUL STATEMENT: [SOUL_STATEMENT]
- controlled surreal event: [SURREAL_EVENT]

Create a clean vertical 2:3 panel for a refined photographic-art quartet. Contemporary ink-like line, dry printed residue, translucent source-colored wash, and restrained collage are allowed. Keep the surface matte, clear, and high-resolution with crisp focal edges, controlled soft transitions, clean negative space, and no compression artifacts. Use one primary mark family and at most two supporting mark families.

Every visible hue and meaningful form must be traceable to the source. Do not default to ivory, beige, gold, gray-green, warm vintage grading, or global desaturation. Do not invent objects, symbols, calligraphy, seals, scenery, or narrative. No dirty parchment, stain field, muddy wash, heavy grain, grunge, fog overlay, vignette, glow, mockup, frame, logo, signature, or illegible text.
```

## Panel 2 suffix — Poetic Distillation

```text
Make the photograph recognizable through relationships rather than literal redraw. Use one broad atmospheric field, the principal subject line, one observed rhythm, one or two identity cues, and one scarce accent. Let the controlled surreal event begin quietly: transform the behavior of the real subject line while retaining the actual subject identity. Route one reduced contour toward the lower-left corner so it can visually approach the future central junction. Keep the whole panel active but uncluttered; no miniature illustration and no centered icon.
```

## Panel 3 suffix — Rhythmic Structure

```text
Remove literal depiction and create a full-panel visual score from the source axis, intervals, count groups, depth, reflections, pauses, and density changes. Use one dominant structural mark family and at most two supporting families. Carry the principal subject line from the upper-right vicinity of this panel toward the central junction, then let it break into measured source-derived rhythm. The result must feel observed, irregular, architectural or organic as appropriate, and never like an infographic or decorative pattern.
```

## Panel 4 suffix — Abstract Soul

```text
Release the SOUL STATEMENT as the strongest and least literal state. Use one large source-colored field, one dominant line or arc crossing most of the panel, one large edge-entering mass, several medium structures, and a small concentrated source accent. Let the controlled surreal event reach its clearest form. Begin one relationship near the upper-left corner so it appears to continue from the central junction, then expand it into the quadrant. Keep one crisp identity contour inside broader controlled ink diffusion. Bold and immersive, yet minimal, clean, and source-bound.
```

## Junction overlay prompt

Generate a separate transparent-background RGBA asset when the image tool supports transparency:

```text
Create one isolated, clean central-junction collage motif derived only from the supplied photograph. Combine [SMALL_SOURCE_SUBJECT_FRAGMENT] with the principal subject line [PRINCIPAL_SUBJECT_LINE]. The fragment should appear to transition from photographic or printed evidence into a precise ink contour, then into two or three sparse rhythmic traces aimed toward [TARGET_QUADRANTS]. Use only [DARK_STRUCTURAL_COLOR] and a very small amount of [ACCENT_COLOR]. Keep the silhouette specific to the photographed subject. Wide transparent margins, no rectangle, no paper card, no sticker edge, no circle badge, no drop shadow, no typography, no invented object, no dense splatter, and no dirty texture. Museum-grade clean cutout, high-resolution edges, subtle material variation, transparent background.
```

If reliable transparency cannot be generated, create the motif on a flat chroma key not present in the source and remove that background before assembly. Inspect the alpha edge at full resolution; reject halos, matte fringes, blocky masks, and accidental background rectangles.

## Assembly example

```bash
python3 scripts/assemble_fourgrid.py \
  /absolute/path/source.jpg \
  /absolute/path/panel-2.png \
  /absolute/path/panel-3.png \
  /absolute/path/panel-4.png \
  /absolute/path/final.png \
  --fill '#SOURCE_DERIVED_HEX' \
  --source-mode contain \
  --bridge /absolute/path/junction-motif.png \
  --bridge-scale 0.16 \
  --bridge-x 0.50 \
  --bridge-y 0.50
```

Use a smaller `--bridge-scale` when the motif approaches the protected anchor. Omit typography from image generation unless exact text will be added deterministically afterward.
