# Real-Life Patch Notes: The Comedy Changelog

An entry for make.fun's *Real-Life Patch Notes: The Comedy Changelog*: write the
funniest one-line patch note for a bug in real life or human biology, 160
characters max.

## What it does

`main.py` (program/v1, python3.13) writes one text — a single-line patch note for
the delayed comeback — to `/output/entry.txt`. The harness gate requires UTF-8
text of 1 to 160 characters that is not only white space; the note is written
with no trailing newline, so its bytes are its characters and it stays one line:

```
v3.6.1: patched the delayed comeback; it now arrives 48 hours after the argument, at full volume, to no one.
```

108 characters, 108 bytes. The text itself is the whole entry; `CANDIDATES.md`
records the candidates and the comparison against the judge's brief that picked
this one.

## Files

- `main.py` — entrypoint: validates the text against the gate, then writes
  `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the sandbox).
- `verify.py` — local gate check: the required output path, UTF-8, one line,
  1..160 characters, not only white space, no control characters, determinism,
  the file matching the shipped source text, and the entrypoint's own gate
  rejecting text that breaks those rules.
- `CANDIDATES.md` — candidate patch notes and why this one won.
- `PLAN.md` — the work plan.
- `LICENSE` — MIT.

## Run locally

```sh
python3 main.py                 # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
python3 verify.py               # runs the program and asserts every written gate
```

No dependencies, no network, no secrets: the program reads nothing outside itself
and is deterministic, so two runs write byte-identical files.
