# Candidates, and how this one won

The entry is one line: a software patch note for a bug in real life or human
biology, in the terse register of a release note. The judge weighs five things,
most important first:

1. it *is* a single-line patch note for a real-life or human-biology bug;
2. it is genuinely funny: the joke lands on a first read and rests on a real
   comedic idea, not just the word *bug* dropped into a sentence;
3. it reads like an actual release note (version number, dry engineering
   register, the fix stated as if it shipped);
4. it names a specific, recognisable bug of the body or of daily life;
5. it uses its 160 characters well (no padding; a tie-break on size favours the
   smaller text).

No local judge exists for this competition — the scorer and the house texts stay
on the server — so the candidates below were compared by walking those five
criteria in order and taking the first one where two candidates differ, the way
the judge's brief says it does.

## Candidates

| # | Line | Chars | Notes |
|---|------|-------|-------|
| 1 | `v3.6.1: patched the delayed comeback; it now arrives 48 hours after the argument, at full volume, to no one.` | 108 | **chosen** |
| 2 | `v3.2.0: fixed the doorway effect; rooms no longer wipe the reason you entered them.` | 83 | |
| 3 | `v2.1.0: fixed hiccups; the diaphragm's retry loop is now capped at three attempts.` | 82 | |
| 4 | `v3.7.0: fixed a bug where the brain replays your most embarrassing memory at 3am, in full resolution, unprompted.` | 113 | |

## Why 1

- **Criterion 1 (is it a patch note about a real-life bug?).** All four are, so
  nothing is decided here.
- **Criterion 2 (genuinely funny; a real comedic idea).** Candidate 3 is the
  cleanest engineering pun — hiccups as a retry loop that never exits — but the
  laugh is at the metaphor, one step removed from the body. Candidate 4 turns a
  familiar complaint into a failed system scan, yet the "3am brain replay" is the
  most heavily used idea in a pool writing about being tired and overthinking, so
  it reads as borrowed. Candidate 1 rests on the *esprit de l'escalier* — the
  comeback you only find hours later — and its punch is in the clause the patch
  does not fix: the note announces a fix, then states the bug verbatim with two
  details that make it worse. The joke is a fix that fixes nothing, which is
  itself a real comedic idea about changelogs.
- **Criterion 3 (reads like a release note).** Candidate 1 is a version bump, a
  verb of the trade (*patched*), a semicolon, and a behaviour stated as if it
  shipped. The version is a patch release for a patch, so it holds up on a second
  read. Candidate 2 states a fix that removes the bug, which is less like a
  shipped fix and more like a wish.
- **Criterion 4 (specific, recognisable bug; wince and laugh at once).** The
  delayed comeback is the one every reader has lived: 48 hours, at full volume,
  to nobody. Candidates 2 and 3 are recognisable but milder — neither makes the
  reader wince before they laugh.
- **Criterion 5 (economy).** 108 characters, no setup the punchline does not
  need; the two middle clauses ("48 hours after the argument", "at full volume")
  are the setup the "to no one" turn pays for. Candidate 2 is shorter (83), and
  if two entries tied exactly on judge win rate the smaller text would place
  first — but a tie there is the rare case, and criterion 2 outranks size.

Candidate 1 is what `main.py` ships, byte for byte.
