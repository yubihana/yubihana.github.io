---
name: filename-watermark
description: Add text watermarks to images using each file's name (before extension). Use this when the user asks to batch watermark JPG/JPEG/PNG files with filename text and control position, color, and font scaling.
---

# Filename Watermark

Use this skill to batch-apply text watermarks to images where watermark text comes from each file's stem.

## When to use

- User asks for filename-based watermarking (example: `A1.jpg` -> `A1`)
- User asks to batch-process images in a folder tree
- User wants watermark controls such as position, color, or scale multiplier

## Requirements

- `python3`
- `Pillow` (`python3-pil` on Debian/Ubuntu)

## Workflow

1. Discover target images:
   - `rg --files -g '*.jpg' -g '*.jpeg' -g '*.png'`
2. Run the script:
   - `python3 skills/filename-watermark/scripts/watermark_images.py --root .`
3. Adjust options as needed:
   - `--position bottom-right|center`
   - `--color black|white`
   - `--size-multiplier 1.0` (or `3.0` to triple)
   - `--no-box` to disable background box
4. Confirm result count from script output.

## Commands

Default (bottom-right, white text, contrast box):

```bash
python3 skills/filename-watermark/scripts/watermark_images.py --root .
```

Centered, black text, 3x size:

```bash
python3 skills/filename-watermark/scripts/watermark_images.py \
  --root . \
  --position center \
  --color black \
  --size-multiplier 3
```
