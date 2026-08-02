"""Generate pixel_avatar.svg: a real GitHub avatar, dithered to black & white,
revealed pixel-by-pixel in a looping terminal-style animation.

No third-party rendering service — pure local image processing (Pillow) plus a
hand-built SVG with CSS keyframe animations, so it can't go down or rate-limit
like the hosted pixel-art-card generators.

Usage:
    pip install pillow requests
    python scripts/make_pixel_avatar.py [github-username]
"""

import sys
import urllib.request
from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = REPO_ROOT / "pixel_avatar.svg"

GRID = 52       # cells per side
CELL = 9        # px per cell in the SVG's own coordinate space
PAD = 18        # frame padding
BG = "#0b1220"
FRAME = "#24303c"
DOT = "#e6edf3"
ACCENT = "#3fc6c0"
CYCLE = 7.0     # full loop, seconds: reveal -> hold -> fade -> hold(empty) -> repeat


def fetch_avatar(username: str, tmp_path: Path) -> Path:
    import json

    with urllib.request.urlopen(f"https://api.github.com/users/{username}") as resp:
        avatar_url = json.load(resp)["avatar_url"]
    urllib.request.urlretrieve(f"{avatar_url}&s=400", tmp_path)
    return tmp_path


def build_svg(image_path: Path) -> str:
    img = Image.open(image_path).convert("L").resize((GRID, GRID), Image.LANCZOS)
    bw = img.convert("1")  # Floyd-Steinberg dithering (Pillow's default)
    pixels = bw.load()

    cells = [
        (row, col)
        for row in range(GRID)
        for col in range(GRID)
        if pixels[col, row] == 0  # '1' mode: 0 = black (the ink we want to show)
    ]

    # Reveal order: diagonal wavefront (row+col) -- reads as a sweep down-and-across
    # rather than a plain top-to-bottom scan, closer to "materializing" than scanning.
    max_wave = (GRID - 1) * 2
    stagger = 1.6 / max_wave  # spread the reveal across ~1.6s of the cycle

    size = GRID * CELL
    total = size + PAD * 2

    parts = [
        f'<svg width="{total}" height="{total}" viewBox="0 0 {total} {total}" '
        f'xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="Pixel-dithered portrait, revealed cell by cell">',
        f'<style>'
        f'.p{{animation: reveal {CYCLE}s ease-in-out infinite;}}'
        f'@keyframes reveal {{'
        f'0% {{ opacity: 0; }} 8% {{ opacity: 1; }} 55% {{ opacity: 1; }} '
        f'70% {{ opacity: 0; }} 100% {{ opacity: 0; }}'
        f'}}'
        f'</style>',
        f'<rect width="{total}" height="{total}" rx="14" fill="{BG}" stroke="{FRAME}" stroke-width="2"/>',
    ]

    for row, col in cells:
        delay = round((row + col) * stagger, 3)
        x = PAD + col * CELL
        y = PAD + row * CELL
        color = ACCENT if (row + col) % 17 == 0 else DOT
        parts.append(
            f'<rect class="p" x="{x}" y="{y}" width="{CELL - 1.4}" height="{CELL - 1.4}" '
            f'rx="1.5" fill="{color}" style="animation-delay:{delay}s"/>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "divyaanshkumar24"
    avatar_path = fetch_avatar(username, REPO_ROOT / ".avatar_tmp.png")
    svg = build_svg(avatar_path)
    OUT_PATH.write_text(svg)
    avatar_path.unlink()
    print(f"wrote {OUT_PATH}")
