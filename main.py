#!/usr/bin/env python3
"""One Line, One Chill - make.fun bounty entry.

Writes a single line of horror to /output/entry.txt.
Deterministic: every run produces identical bytes, no trailing newline.

makefun anchor 36b260016453a4c632d4d2c8fc7d90c5ae8496d7 round 34246377
"""

import os

ENTRY = (
    "Semalam aku merekam tidurku untuk membuktikan tidak ada yang masuk kamar, "
    "dan pagi ini videonya menunjukkan aku berdiri di samping tempat tidur, "
    "menatap diriku sendiri tanpa pernah berkedip."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
