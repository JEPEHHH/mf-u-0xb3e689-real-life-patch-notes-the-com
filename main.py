#!/usr/bin/env python3
"""make.fun entry: Real-Life Patch Notes: The Comedy Changelog (program/v1).

The competition's program/v1 harness runs this entrypoint (main.py, python3.13) in
a sandbox with no network, then a sealed scorer reads what it wrote. The entry has
to write one text to /output/entry.txt (the harness mounts the output directory at
/output; the program's own working directory is the repository).

The gate: /output/entry.txt is UTF-8 text of 1 to 160 characters and not only white
space. The judge then compares the text, two entries at a time, for the funniest
one-line patch note for a bug in real life or human biology.

So this program does exactly one thing, deterministically: it writes the chosen
patch note to entry.txt with no trailing newline, so the byte count equals the
character count and the single-line rule holds.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entry (see CANDIDATES.md for the candidates and why this one won).
# One line, the terse register of a real release note, a real bug of daily life,
# and the punch in the clause the patch does not fix.
ENTRY = "v3.6.1: patched the delayed comeback; it now arrives 48 hours after the argument, at full volume, to no one."

# The gate the sealed scorer checks, kept here so the entry can refuse to write an
# invalid entry.txt rather than lose the grade to a typo.
MIN_CHARS = 1
MAX_CHARS = 160


def validate(entry: str) -> str:
    """Hold `entry` to the gate: 1..160 characters, one line, not only white space."""
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} characters, outside {MIN_CHARS}..{MAX_CHARS}")
    if entry.strip() == "":
        raise ValueError("entry is only white space")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry is not a single line")
    return entry


def output_dir() -> Path:
    """The directory entry.txt goes in.

    /output inside the harness sandbox. Outside it, MAKEFUN_OUTPUT_DIR (the kit's
    own convention) overrides the location so the program can be run and checked
    locally without writing to /output.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def write_entry(target: Path) -> Path:
    """Write the (validated) entry to <target>/entry.txt, one line, no trailing newline."""
    text = validate(ENTRY)
    target.mkdir(parents=True, exist_ok=True)
    entry = target / "entry.txt"
    entry.write_text(text, encoding="utf-8", newline="")
    return entry


def main() -> int:
    entry = write_entry(output_dir())
    print(f"wrote {len(ENTRY)} chars ({len(ENTRY.encode('utf-8'))} bytes) to {entry}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
