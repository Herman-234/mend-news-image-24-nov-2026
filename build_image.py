#!/usr/bin/env python3
"""Draw the 24 Nov 2026 world-news front page as a 1024x1024 PNG.

Pure stdlib + Pillow, no network, no randomness, no clock reads:
the same run always writes the same bytes.
Usage: python3 build_image.py   -> writes entry.png beside this file.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = "/usr/share/fonts/truetype/dejavu"

SIZE = 1024
PAPER = (246, 242, 235)
NAVY = (18, 32, 62)
GOLD = (250, 160, 18)
CARD = (255, 255, 255)
INK = (26, 26, 26)
GREY = (96, 96, 96)
SOFT = (236, 236, 236)


def load(name, size):
    return ImageFont.truetype(os.path.join(FONT_PATH, name), size)


TITLE_F = load("DejaVuSans-Bold.ttf", 54)
DATE_F = load("DejaVuSans-Bold.ttf", 26)
HEAD_F = load("DejaVuSans-Bold.ttf", 32)
BODY_F = load("DejaVuSans.ttf", 22)
TAG_F = load("DejaVuSans-Bold.ttf", 18)
FOOT_F = load("DejaVuSans.ttf", 19)


def wrap_text(text, font, width):
    """Greedy word wrap returning a list of lines fitting `width`."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if font.getlength(trial) <= width:
            current = trial
        elif current:
            lines.append(current)
            current = word
        else:
            current = word
    if current:
        lines.append(current)
    return lines


def globe(draw, cx, cy, r, colour):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=colour, width=6)
    draw.ellipse([cx - r * 0.4, cy - r, cx + r * 0.4, cy + r],
                 outline=colour, width=4)
    draw.line([cx - r, cy, cx + r, cy], fill=colour, width=4)
    draw.arc([cx - r, cy - r * 0.5, cx + r, cy + r * 0.5],
             200, 340, fill=colour, width=4)


def flame(draw, cx, cy, r, colour):
    points = [
        (cx, cy - r), (cx + r * 0.5, cy - r * 0.35),
        (cx + r * 0.8, cy + r * 0.25), (cx + r * 0.4, cy + r * 0.7),
        (cx + r * 0.12, cy + r * 0.4), (cx - r * 0.2, cy + r * 0.8),
        (cx - r * 0.65, cy + r * 0.45), (cx - r * 0.55, cy - r * 0.15),
    ]
    draw.polygon(points, fill=colour)


def burst(draw, cx, cy, r, colour):
    points = []
    for i in range(16):
        angle = math.pi * i / 8.0
        dist = r if i % 2 == 0 else r * 0.42
        points.append((cx + dist * math.cos(angle),
                       cy + dist * math.sin(angle)))
    draw.polygon(points, fill=colour)


def train(draw, cx, cy, r, colour):
    x0, y0 = cx - r, cy - r * 0.65
    x1, y1 = cx + r, cy + r * 0.5
    draw.rounded_rectangle([x0, y0, x1, y1], radius=12, fill=colour)
    for i in range(3):
        wx = x0 + 12 + i * 34
        draw.rectangle([wx, y0 + 12, wx + 24, y0 + 36], fill=(255, 255, 255))
    for off in (-0.5, 0.25):
        wx = cx + off * r
        draw.ellipse([wx - 11, y1 - 4, wx + 11, y1 + 18], fill=INK)


def chart(draw, cx, cy, r, colour):
    pts = [
        (cx - r, cy - r * 0.45), (cx - r * 0.35, cy - r * 0.05),
        (cx, cy - r * 0.3), (cx + r * 0.4, cy + r * 0.35),
        (cx + r, cy + r * 0.8),
    ]
    draw.line(pts, fill=colour, width=8, joint="curve")
    draw.polygon([
        (cx + r, cy + r * 0.8), (cx + r - 6, cy + r * 0.8 - 26),
        (cx + r - 26, cy + r * 0.8 - 4),
    ], fill=colour)


ICONS = {"globe": globe, "flame": flame, "burst": burst,
         "train": train, "chart": chart}


# (tag, accent colour, headline, deck, icon key)
STORIES = [
    ("CLIMATE", (196, 88, 38), "COP31 ENDS WITHOUT A DEAL",
     "Climate talks in Antalya close with no agreement on fossil fuels.",
     "globe"),
    ("DISASTER", (210, 46, 48), "FACTORY FIRE IN INDONESIA",
     "Fire in Banten kills at least 24; rescuers search for about 30 missing.",
     "flame"),
    ("WAR", (30, 88, 158), "UKRAINE WAR GRINDS ON",
     "Russian drone strike hits the Kyiv region; Russian war dead put above 700,000.",
     "burst"),
    ("DIPLOMACY", (38, 118, 68), "INDIA-NEPAL RAIL LINK OPENS",
     "Modi and Shah flag off the Saryu-Kamala Express; India pledges a Rs 15,000-crore package.",
     "train"),
    ("MARKETS", (138, 28, 28), "WALL STREET TUMBLES",
     "Stocks shed $1 trillion after the Democrats' midterm win; Trump blames Democrats.",
     "chart"),
]


def draw_card(draw, y0, y1, story):
    tag, accent, headline, deck, icon_key = story
    draw.rounded_rectangle([24, y0, SIZE - 24, y1], radius=18, fill=CARD)
    draw.rectangle([24, y0 + 14, 34, y1 - 14], fill=accent)
    # icon tile on the left
    cx, cy, rad = 116, (y0 + y1) // 2, 50
    draw.rounded_rectangle([cx - rad, cy - rad, cx + rad, cy + rad],
                           radius=16, fill=SOFT)
    ICONS[icon_key](draw, cx, cy, 30, accent)
    # tag pill, top right
    tag_w = TAG_F.getlength(tag)
    draw.text((SIZE - 48 - tag_w, y0 + 16), tag, font=TAG_F, fill=accent)
    # headline and deck
    tx = 192
    draw.text((tx, y0 + 18), headline, font=HEAD_F, fill=INK)
    lines = wrap_text(deck, BODY_F, SIZE - 48 - tx)
    ly = y0 + 66
    for line in lines[:2]:
        draw.text((tx, ly), line, font=BODY_F, fill=GREY)
        ly += 29


def render():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)
    # masthead
    draw.rectangle([0, 0, SIZE, 122], fill=NAVY)
    draw.rectangle([0, 122, SIZE, 128], fill=GOLD)
    title = "THE WORLD IN ONE IMAGE"
    draw.text(((SIZE - TITLE_F.getlength(title)) / 2, 16), title,
              font=TITLE_F, fill=(255, 255, 255))
    date = "TUESDAY  ·  24 NOVEMBER 2026"
    draw.text(((SIZE - DATE_F.getlength(date)) / 2, 80), date,
              font=DATE_F, fill=GOLD)
    # five story cards
    top, height, gap = 146, 160, 10
    for i, story in enumerate(STORIES):
        y0 = top + i * (height + gap)
        draw_card(draw, y0, y0 + height, story)
    # footer with the real sources
    foot = ("Sources: Jagran Josh  ·  StudMentor  ·  ObserverVoice  ·  "
            "Global24  —  24 Nov 2026")
    draw.text(((SIZE - FOOT_F.getlength(foot)) / 2, SIZE - 36), foot,
              font=FOOT_F, fill=GREY)
    return img


if __name__ == "__main__":
    out = os.path.join(BASE, "entry.png")
    render().save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")
