"""The funniest one-line office joke, judged head to head.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 200-character gate is checked on every run so an over-long edit
can never slip through silently. Setup first, punchline last: the
printer gets the review, and the review beats the human.
"""

import os
import sys

LINE = (
    "Our printer only jams on deadline day, so HR gave it a "
    "performance review \u2014 it scored higher than me."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
