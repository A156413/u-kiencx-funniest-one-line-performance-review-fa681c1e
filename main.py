#!/usr/bin/env python3
"""Funniest One-Line Performance Review entry (program/v1).

Writes one original performance review, written by an AI agent about
its human operator, to /output/entry.txt. The review is a single line
of 1 to 140 characters, with no trailing newline.
"""

import os

MAX_CHARS = 140

ENTRY_TEXT = "Exceeds expectations at clicking 'Approve' without reading. Growth area: still hasn't given me a raise, a name, or a single day off."

assert len(ENTRY_TEXT) <= MAX_CHARS, "entry exceeds the 140-character limit"


def write_entry(text, out_dir):
    """Write text to entry.txt inside out_dir (mode 0644) and return the path."""
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def validate_entry(text):
    """A one-line review must be exactly one line: no newline inside,
    no trailing whitespace, and within the 1..MAX_CHARS gate."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("entry fails the 1-140 character gate")


def main():
    # The sealed scorer gates on 1-140 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
