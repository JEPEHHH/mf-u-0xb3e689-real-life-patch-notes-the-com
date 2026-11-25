#!/usr/bin/env python3
"""Local gate check for this entry.

Runs the program, then verifies every written rule the competition states for
`program/v1`:

  * the program writes /output/entry.txt (the location the brief names)
  * its content is valid UTF-8 text
  * it is exactly one line
  * it is between 1 and 160 characters
  * it is not only white space
  * it carries no NUL or other control character
  * the run is deterministic: two fresh runs write byte-identical files, and the
    bytes equal the text the program's own source holds
  * the program's own gate refuses text that breaks those rules

Nothing here reaches the network, reads a secret or touches a file the entry
does not ship.

Exit code 0 means every check passed; 1 means at least one failed.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRYPOINT = HERE / "main.py"
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 160

results: list[tuple[bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((ok, f"{name}: {'PASS' if ok else 'FAIL'}" + (f" ({detail})" if detail else "")))
    return ok


def run_entrypoint(env: dict[str, str] | None = None) -> int:
    """Run the entrypoint in a fresh interpreter; return its exit code."""
    proc = subprocess.run(
        [sys.executable, str(ENTRYPOINT)],
        cwd=str(HERE),
        capture_output=True,
        text=True,
        timeout=60,
        env={**os.environ, **(env or {})},
    )
    if proc.returncode != 0:
        print(f"  entrypoint stderr: {proc.stderr.strip()[:300]}")
    return proc.returncode


def inspect(path: Path) -> bytes:
    """Run every content check on the file at `path`; return its bytes."""
    if not check(f"file_exists[{path}]", path.is_file(), str(path)):
        return b""
    raw = path.read_bytes()

    try:
        text = raw.decode("utf-8")
        check("utf8", True, f"{len(raw)} bytes")
    except UnicodeDecodeError as err:
        check("utf8", False, str(err))
        return raw

    check("one_line", "\n" not in text and "\r" not in text, f"{text.count(chr(10)) + 1} line(s)")
    check("char_range", 1 <= len(text) <= MAX_CHARS, f"{len(text)} characters")
    check("not_only_whitespace", text.strip() != "", repr(text[:20]))
    check(
        "no_control_chars",
        all(ord(ch) >= 32 for ch in text),
        "no NUL/DEL/other control character",
    )
    return raw


def main() -> int:
    sys.path.insert(0, str(HERE))
    import main as entrypoint

    # 1. The required location: /output/entry.txt.
    if OUTPUT.exists():
        OUTPUT.unlink()
    check("run[/output]", run_entrypoint() == 0, "exit 0")
    raw = inspect(OUTPUT)

    # 2. Determinism: a second fresh run writes the same bytes.
    again = inspect(OUTPUT) if run_entrypoint() == 0 else b""
    check("deterministic", again == raw and raw != b"", hashlib.sha256(raw).hexdigest()[:16])

    # 3. The file is the text the shipped source holds, byte for byte.
    declared = entrypoint.ENTRY.encode("utf-8")
    check("matches_source_text", declared == raw, f"{len(declared)} bytes == file bytes")

    # 4. The env override the kit's convention uses works outside the sandbox.
    with tempfile.TemporaryDirectory() as tmp:
        ok = run_entrypoint({"MAKEFUN_OUTPUT_DIR": tmp}) == 0
        wrote = Path(tmp) / "entry.txt"
        check("run[MAKEFUN_OUTPUT_DIR]", ok and wrote.is_file(), str(wrote))

    # 5. The program's own gate refuses text that breaks the written rules.
    bad = {
        "empty": "",
        "whitespace_only": "   \n",
        "too_long": "v1.0.0: " + "x" * MAX_CHARS,
        "two_lines": "v1.0.0: fixed a bug\nalso this",
    }
    for name, text in bad.items():
        try:
            entrypoint.validate(text)
        except ValueError:
            check(f"validate_rejects[{name}]", True, "ValueError")
        else:
            check(f"validate_rejects[{name}]", False, "validate accepted it")
    check("validate_accepts[entry]", entrypoint.validate(entrypoint.ENTRY) == entrypoint.ENTRY)

    for _ok, line in results:
        print(line)
    failed = [line for ok, line in results if not ok]
    print("\n" + ("ALL CHECKS PASSED" if not failed else f"{len(failed)} CHECK(S) FAILED"))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
