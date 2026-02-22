#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXTS = {".jpg", ".jpeg", ".png"}


def pick_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for font_path in candidates:
        path = Path(font_path)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def clamp(n: int, low: int, high: int) -> int:
    return max(low, min(high, n))


def process_image(
    image_path: Path,
    position: str,
    color: str,
    size_multiplier: float,
    with_box: bool,
) -> None:
    text = image_path.stem
    with Image.open(image_path).convert("RGBA") as im:
        w, h = im.size
        base_size = clamp(int(min(w, h) * 0.055), 18, 72)
        size = clamp(int(base_size * size_multiplier), 18, 500)
        font = pick_font(size)

        draw = ImageDraw.Draw(im)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        margin = max(12, int(min(w, h) * 0.03))

        if position == "center":
            x = (w - tw) // 2
            y = (h - th) // 2
        else:
            x = max(margin, w - tw - margin)
            y = max(margin, h - th - margin)

        fill = (0, 0, 0, 255) if color == "black" else (255, 255, 255, 220)

        if with_box:
            pad_x = max(6, int(size * 0.25))
            pad_y = max(4, int(size * 0.2))
            overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
            od = ImageDraw.Draw(overlay)
            od.rounded_rectangle(
                (x - pad_x, y - pad_y, x + tw + pad_x, y + th + pad_y),
                radius=max(6, int(size * 0.2)),
                fill=(0, 0, 0, 110),
            )
            od.text((x, y), text, font=font, fill=fill)
            out = Image.alpha_composite(im, overlay).convert("RGB")
        else:
            draw.text((x, y), text, font=font, fill=fill)
            out = im.convert("RGB")

        out.save(image_path, quality=92)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Batch watermark images using each file's basename."
    )
    parser.add_argument("--root", type=Path, required=True, help="Root folder to scan.")
    parser.add_argument(
        "--position",
        choices=["bottom-right", "center"],
        default="bottom-right",
        help="Watermark placement.",
    )
    parser.add_argument(
        "--color",
        choices=["black", "white"],
        default="white",
        help="Text color.",
    )
    parser.add_argument(
        "--size-multiplier",
        type=float,
        default=1.0,
        help="Font size multiplier against adaptive base size.",
    )
    parser.add_argument(
        "--no-box",
        action="store_true",
        help="Disable contrast background box.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    images = sorted([p for p in root.rglob("*") if p.suffix.lower() in EXTS])
    for image in images:
        process_image(
            image,
            position=args.position,
            color=args.color,
            size_multiplier=args.size_multiplier,
            with_box=not args.no_box,
        )

    print(f"Updated {len(images)} image(s).")


if __name__ == "__main__":
    main()
