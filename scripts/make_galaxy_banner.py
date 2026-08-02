"""Generate banner.svg: a galaxy/constellation header banner.

Starfield with twinkling stars + a constellation of larger stars connected by
thin lines, spelling out the same "retrieve -> route -> execute -> verify"
pipeline motif as the project banners, rendered as a constellation instead of
icons. Plus two shooting stars for motion. Self-contained SVG, no third-party
service -- pure Python + hand-built SVG/CSS.

Usage:
    python scripts/make_galaxy_banner.py
"""

import random
from pathlib import Path

random.seed(7)  # fixed seed so regenerating gives the same star layout

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = REPO_ROOT / "banner.svg"

W, H = 1200, 300
NAME = "Divyaansh Kumar Gupta"
TAGLINE = "Systems that show their work."

BG_TOP = "#05070d"
BG_BOT = "#0d1224"
NEBULA_A = "#2a1a4d"
NEBULA_B = "#0e3a3a"
STAR = "#e6edf3"
STAR_DIM = "#8fa2b8"
CONSTELLATION_STAR = "#7ee8e0"
LINE = "#3fc6c0"

# The pipeline motif, reused across this profile's and my projects' banners.
NODES = {
    "retrieve": (110, 210),
    "route": (300, 165),
    "execute": (490, 215),
    "verify": (690, 160),
}
ORDER = ["retrieve", "route", "execute", "verify"]


def build_svg() -> str:
    parts = [
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="{NAME} -- {TAGLINE.rstrip(chr(46))}, rendered as a constellation">',
        f'''<defs>
  <linearGradient id="sky" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG_TOP}"/>
    <stop offset="100%" stop-color="{BG_BOT}"/>
  </linearGradient>
  <radialGradient id="nebula1" cx="20%" cy="30%" r="60%">
    <stop offset="0%" stop-color="{NEBULA_A}" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="{NEBULA_A}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="nebula2" cx="80%" cy="70%" r="55%">
    <stop offset="0%" stop-color="{NEBULA_B}" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="{NEBULA_B}" stop-opacity="0"/>
  </radialGradient>
  <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
    <feGaussianBlur stdDeviation="2.2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>''',
        f'<rect width="{W}" height="{H}" rx="20" fill="url(#sky)"/>',
        f'<rect width="{W}" height="{H}" rx="20" fill="url(#nebula1)"/>',
        f'<rect width="{W}" height="{H}" rx="20" fill="url(#nebula2)"/>',
        '''<style>
  .tw { animation: twinkle 3.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
  @keyframes twinkle { 0%,100% { opacity: 0.25; } 50% { opacity: 1; } }
  .shoot { animation: shoot 6s linear infinite; }
  @keyframes shoot {
    0% { transform: translate(0,0); opacity: 0; }
    2% { opacity: 1; }
    16% { transform: translate(260px,110px); opacity: 0; }
    100% { transform: translate(260px,110px); opacity: 0; }
  }
  .cstar { animation: cpulse 5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
  @keyframes cpulse { 0%,100% { opacity: 0.75; r: 3.2px; } 50% { opacity: 1; r: 4px; } }
</style>''',
        f'<clipPath id="clip"><rect width="{W}" height="{H}" rx="20"/></clipPath>',
        '<g clip-path="url(#clip)">',
    ]

    for _ in range(160):
        x = random.uniform(0, W)
        y = random.uniform(0, H)
        r = random.uniform(0.5, 1.6)
        dur = random.uniform(2.4, 4.6)
        delay = random.uniform(0, 4)
        color = STAR if random.random() > 0.35 else STAR_DIM
        parts.append(
            f'<circle class="tw" cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{color}" '
            f'style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s"/>'
        )

    for sx, sy, delay in [(120, 40, 0.5), (700, 90, 3.4)]:
        parts.append(
            f'<g class="shoot" style="animation-delay:{delay}s">'
            f'<line x1="{sx}" y1="{sy}" x2="{sx - 38}" y2="{sy - 14}" stroke="{STAR}" stroke-width="1.6" '
            f'stroke-linecap="round" opacity="0.9" filter="url(#glow)"/>'
            f'</g>'
        )

    parts.append('</g>')

    for a, b in zip(ORDER, ORDER[1:]):
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LINE}" '
            f'stroke-width="1.3" opacity="0.55"/>'
        )

    for i, key in enumerate(ORDER):
        x, y = NODES[key]
        delay = i * 0.4
        parts.append(
            f'<circle class="cstar" cx="{x}" cy="{y}" r="3.6" fill="{CONSTELLATION_STAR}" '
            f'filter="url(#glow)" style="animation-delay:{delay}s"/>'
        )
        parts.append(
            f'<text x="{x}" y="{y + 22}" font-family="Menlo, Consolas, monospace" font-size="12" '
            f'fill="{STAR_DIM}" text-anchor="middle">{key}</text>'
        )

    parts.append(f'''<g font-family="Menlo, Consolas, monospace" text-anchor="end">
  <text x="1160" y="120" font-size="32" font-weight="700" fill="{STAR}">{NAME}</text>
  <text x="1160" y="150" font-size="15" fill="{STAR_DIM}">{TAGLINE}</text>
</g>''')

    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    OUT_PATH.write_text(build_svg())
    print(f"wrote {OUT_PATH}")
