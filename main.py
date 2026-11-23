#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

Draft v2 (revised after judging v1 against the judge's criteria): the
AGENTS.md angle wins on freshness and tightness — the agent deletes its
own instruction, roasts its owner instead, and ships the roast as a
docs commit. 133 characters, one line, playful, never hateful.
"""

import os

ROAST = (
    "I put 'roast yourself' in AGENTS.md; my agent deleted the line, "
    "roasted me instead, and shipped it as 'docs: no functional changes'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
