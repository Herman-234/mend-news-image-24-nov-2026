#!/usr/bin/env python3
"""Entrypoint for the news-image-20261124 bounty.

Writes the entry image to the output directory as entry.png.
No network, no randomness: the bytes copied are the bytes of the
pre-rendered image held in this repository, so every run writes
the exact same file.

The grader runs this program twice; both runs must produce
identical output, which a plain byte copy guarantees.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def output_dir():
    """Grader output dir, overridable for local checks."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    source = os.path.join(HERE, SOURCE_NAME)
    if not os.path.isfile(source):
        print("missing:", source, file=sys.stderr)
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    with open(source, "rb") as fh:
        data = fh.read()
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "wb") as fh:
        fh.write(data)
    print("wrote", target, len(data), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
