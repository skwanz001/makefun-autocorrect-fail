"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt.
Standard library only: the grading sandbox installs nothing.
"""

import os

ENTRY = (
    "Meant to text my crush 'you're cute' \u2014 autocorrect sent "
    "'you're a cult' and she replied 'finally, someone who gets me.'"
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
    # not only white space. Fail loudly here rather than shipping invalid.
    if not 1 <= len(ENTRY) <= 199 or not ENTRY.strip():
        raise ValueError(f"entry violates the gate: {len(ENTRY)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
