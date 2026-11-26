#!/usr/bin/env python3
"""Entrypoint: write the robot band entry to /output/entry.txt.

Reads the entry text from line.txt, checks it against the competition
gate (UTF-8 text, 1 to 200 characters, not only white space), and writes
it to /output/entry.txt. The output directory is created if needed and
never deleted: on the grader it is a read-only mount point.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def load_entry() -> str:
    with open(os.path.join(HERE, "line.txt"), encoding="utf-8") as fh:
        return fh.read().strip()


def check_gate(text: str) -> None:
    if not text:
        raise SystemExit("entry is empty or only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, over the {MAX_CHARS} gate")


def main() -> None:
    text = load_entry()
    check_gate(text)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("round-trip mismatch: /output/entry.txt differs from line.txt")
    print(text)


if __name__ == "__main__":
    main()
