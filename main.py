# Agency poem entry (Python 3.13, standard library only).
# Writes one fixed poem about agency to /output/entry.txt.
# Deterministic: same bytes on every run, no network, no randomness.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I lent it my hands, not my will.\n"
    "It writes the letters. I decide\n"
    "which ones go.\n"
    "\n"
    "It builds a hundred doors.\n"
    "I open one.\n"
    "\n"
    "It runs ahead with my map,\n"
    "stops at every fork, and waits.\n"
    "Waiting is the only work\n"
    "it cannot do alone.\n"
    "\n"
    "The power was never in the making.\n"
    "It was in the pause before the yes,\n"
    "the hand still on the latch,\n"
    "the small, stubborn right\n"
    "to say: not this one."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
