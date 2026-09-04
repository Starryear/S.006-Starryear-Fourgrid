---
name: starryear-fourgrid
description: Transform one user-supplied photograph into a clean vertical 2×2 Starryear quartet that moves from photographic evidence to poetic distillation, rhythmic structure, and abstract soul, joined by one source-derived central motif. Use for Starryear-Fourgrid, 水墨四宫格, 照片一变四, or source-bound photographic abstraction. Do not use for ordinary collages, four filters, generic ink landscapes, or full-frame photo stylization.
metadata:
  author: "Starryear年"
  version: "2.1.0"
  license: "Starryear Personal and Non-commercial Use License"
---

# Starryear-Fourgrid

Create one vertical 2:3 bitmap from exactly one user-supplied photograph. Arrange four equal vertical 2:3 cells as `Evidence → Poetic Distillation → Rhythmic Structure → Abstract Soul`, then connect the central cross with one small source-derived subject-line motif. Panel 1 must contain the actual source pixels; Panels 2–4 reinterpret only observable source evidence.

## Efficient workflow

1. Require exactly one authorized source photograph and inspect it once. If none is available, ask for it and stop.
2. Read one full prompt only: use the Chinese prompt by default, or the English prompt when the user requests English. Complete the compact source lock in [references/source-analysis.md](references/source-analysis.md) internally; do not output the analysis.
3. Protect the primary subject, viewpoint, meaningful count, light, color balance, and one decisive contour. Choose one `SOUL STATEMENT`, one source-bound surreal event, and one junction motif.
4. Generate Panels 2–4 as separate vertical 2:3 images, scheduling the independent generations in parallel when supported. Generate one transparent junction asset from the same locked source facts. Never generate Panel 1.
5. Assemble the actual photograph, the three generated panels, a 2–6 px source-colored divider, and the junction asset with [scripts/assemble_fourgrid.py](scripts/assemble_fourgrid.py).
6. Perform one final review using [references/quality-gate.md](references/quality-gate.md): confirm source lock, four-state progression, junction transparency, 2:3 geometry, clean surface, and minimum resolution. Do not repeat checks when no concrete defect is visible.
7. If an asset fails, fix assembly deterministically or regenerate only that failed panel or junction once. Never restart the whole sequence and never regenerate Panel 1.

## Fixed output

- One RGB/sRGB PNG, preferably 3072×4608 and never below 2048×3072.
- True 2×2 grid: Evidence top-left, Poetic Distillation top-right, Rhythmic Structure bottom-left, Abstract Soul bottom-right.
- Four complete compositions connected by one restrained central motif covering about 3–8% of the master.
- No outer frame, rounded cards, mockup, fifth panel, logo, signature, watermark, or generated pseudo-text.
- Default to no typography. Add exact text deterministically only when the user asks.

## Guardrails

- Panel 1 permits proportional scaling, crop, or source-derived padding only—no redraw, retouch, recolor, filtering, extension, or replacement.
- Every important hue, form, rhythm, and surreal behavior in Panels 2–4 must trace to visible source evidence.
- Use one primary mark family and no more than two supporting families; keep texture local and low-amplitude.
- Reject generic beige editorial presets, unrelated fantasy symbols, traditional ink-landscape clichés, dirty parchment, heavy grain, muddy wash, dense splatter, thick seams, dead corners, and tiny centered icons.
- Preserve faces, gestures, animal identity, architectural anchors, reflections, and meaningful counts whenever they define the photograph.

## Full prompts and focused references

- Chinese full prompt: [references/starryear-fourgrid-prompt.zh-CN.md](references/starryear-fourgrid-prompt.zh-CN.md)
- English full prompt: [references/starryear-fourgrid-prompt.en.md](references/starryear-fourgrid-prompt.en.md)
- Additional art direction: [references/art-direction.md](references/art-direction.md)
- Tool-specific prompt blocks: [references/production-prompts.md](references/production-prompts.md)

Do not read the additional art-direction and production-prompt files during the default fast path unless a subject needs clarification or a generated component fails.

Keep [assets/examples](assets/examples) empty during drafting and testing. After Starryear年 explicitly accepts the tested Skill, add only final images supplied or approved by the user. Treat them as examples only and never reuse their subjects, palettes, or composition unless the user supplies that exact image.
