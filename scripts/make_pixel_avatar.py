"""Generate pixel_avatar.svg: a real GitHub avatar, quantized to a handful of
monochrome-plus-accent tone levels, revealed pixel-by-pixel in a looping
terminal-style animation.

No third-party rendering service — pure local image processing (Pillow) plus a
hand-built SVG with CSS keyframe animations, so it can't go down or rate-limit
like the hosted pixel-art-card generators.

Design notes (v2, after the first pass looked noisy):
  - Tone-level quantization instead of Floyd-Steinberg dithering. Binary
    dithering on a real photo at low resolution produces salt-and-pepper noise
    that reads as "low quality"; discrete tone buckets read as clean pixel art.
  - Cells are fully contiguous (no gaps) -- gaps between dots read as a dot
    matrix, not pixel art.
  - shape-rendering="crispEdges" on the SVG root -- without it, browsers
    anti-alias the seams between same-color adjacent cells whenever the image
    is scaled to a display size that isn't the SVG's native pixel grid,
    producing faint grid-line artifacts.

Usage:
    pip install pillow
    python scripts/make_pixel_avatar.py [github-username]
"""

import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = REPO_ROOT / "pixel_avatar.svg"

GRID = 64       # cells per side
CELL = 8        # px per cell in the SVG's own coordinate space
PAD = 16        # frame padding
BG = "#0b1220"
FRAME = "#24303c"
CYCLE = 7.0     # full loop, seconds: reveal -> hold -> fade -> hold(empty) -> repeat

# Monochrome ramp from background-ish dark up through mid grays to bright white,
# with the single brightest bucket tipped to the teal accent used elsewhere in
# the profile, for a bit of duotone "shimmer" rather than flat grayscale.
LEVELS = ["#1c2838", "#334357", "#57708c", "#8fa2b8", "#cbd5e1", "#e6edf3", "#7ee8e0"]
N_LEVELS = len(LEVELS)


def fetch_avatar(username: str, tmp_path: Path) -> Path:
    import json

    with urllib.request.urlopen(f"https://api.github.com/users/{username}") as resp:
        avatar_url = json.load(resp)["avatar_url"]
    urllib.request.urlretrieve(f"{avatar_url}&s=400", tmp_path)
    return tmp_path


def build_svg(image_path: Path) -> str:
    img = Image.open(image_path).convert("L")
    img = ImageEnhance.Contrast(img).enhance(1.25)
    img = ImageEnhance.Brightness(img).enhance(1.05)
    img = img.resize((GRID, GRID), Image.LANCZOS)
    pixels = img.load()

    size = GRID * CELL
    total = size + PAD * 2
    max_wave = (GRID - 1) * 2
    stagger = 1.6 / max_wave  # spread the reveal across ~1.6s of the cycle

    parts = [
        f'<svg width="{total}" height="{total}" viewBox="0 0 {total} {total}" '
        f'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges" role="img" '
        f'aria-label="Pixelated portrait, revealed cell by cell">',
        f'<style>'
        f'.p{{animation: reveal {CYCLE}s ease-in-out infinite;}}'
        f'@keyframes reveal {{'
        f'0% {{ opacity: 0; }} 8% {{ opacity: 1; }} 55% {{ opacity: 1; }} '
        f'70% {{ opacity: 0; }} 100% {{ opacity: 0; }}'
        f'}}'
        f'</style>',
        f'<rect width="{total}" height="{total}" rx="14" fill="{BG}" stroke="{FRAME}" stroke-width="2"/>',
    ]

    for row in range(GRID):
        for col in range(GRID):
            level = min(pixels[col, row] * N_LEVELS // 256, N_LEVELS - 1)
            if level == 0:
                continue  # let the background show through for the darkest tone
            delay = round((row + col) * stagger, 3)
            x = PAD + col * CELL
            y = PAD + row * CELL
            parts.append(
                f'<rect class="p" x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
                f'fill="{LEVELS[level]}" style="animation-delay:{delay}s"/>'
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
