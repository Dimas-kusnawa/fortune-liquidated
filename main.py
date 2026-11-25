#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who has just
been liquidated, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os

# Gate check: 19 words (cap 20) and 98 characters (gate 1-160),
# one line, no trailing newline, UTF-8 plain text.
LINE = "You will meet a tall, dark stranger: your margin call, arriving at 3 a.m. to collect what you owe."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
