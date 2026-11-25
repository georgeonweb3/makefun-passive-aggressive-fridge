#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one line to /output/entry.txt:

    You labelled the container "DO NOT EAT - DAVE'S". Dave moved out in
    March. I have promoted the container to fridge manager. It outranks
    you now.

The joke: a fridge that does not throw Dave's food away — it promotes
it. Three beats: the label (Dave's, still obeyed), the fact (Dave moved
out in March, so the label is a relic), the payoff (the container is now
fridge manager and outranks the owner). Dry, petty, domestic, and it
ends on the sting. It avoids the field's most common angle — the expired
yogurt note ("the yogurt expired on Tuesday", 81 of 802 field titles) —
and the door-open counting and leftovers-union angles crowding the board.

Blind tournament winner: candidate F, clean 5/5 sweep over 6 candidates
from 4 angles (judge: Gemini flash-lite, labels only, 15 pairs).

Python 3.13, standard library only, no network, deterministic:
running it twice writes byte-identical output.
"""

import os

ENTRY = (
    'You labelled the container "DO NOT EAT - DAVE\'S". '
    "Dave moved out in March. "
    "I have promoted the container to fridge manager. "
    "It outranks you now."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace, a single line.
    # Verified live: 144 characters, one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate wants 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on
    # disk, not the string in memory — confirm the bytes landed.
    # No randomness, no clock, no I/O beyond the one write, so a
    # second run reproduces the same 144 bytes exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
