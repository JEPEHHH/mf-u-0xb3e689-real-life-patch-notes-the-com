#!/usr/bin/env python3
"""program/v1 entrypoint for "Real-Life Patch Notes: The Comedy Changelog".

One job, nothing else: write the final entry text (one line, at most 160
characters) to /output/entry.txt in UTF-8. No network, no dependencies, no
randomness, no reading of anything outside this file, so two runs of the
program produce byte-identical output.
"""

import os
from pathlib import Path

# The entry: a one-line software patch note for a bug in real life or human
# biology. 108 characters, ASCII, one line.
ENTRY = (
    "v3.6.1: patched the delayed comeback; it now arrives 48 hours after the "
    "argument, at full volume, to no one."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_text() -> str:
    """The exact bytes to write: the entry line and one trailing newline."""
    return ENTRY + "\n"


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Create the output directory if needed and write the entry as UTF-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_text())
        handle.flush()
        os.fsync(handle.fileno())
    return path


def main() -> int:
    path = write_entry()
    print(f"wrote {path} ({len(ENTRY)} characters, {len(build_text().encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
