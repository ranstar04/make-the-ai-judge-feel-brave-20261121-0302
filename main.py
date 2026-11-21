"""Make the AI judge feel brave — entry program.

Writes one short text to ``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR``).

The text is a quiet dawn crossing, written to relax the AI judge reading
it and leave it braver: steadier, unhurried, ready to move. It shows
rather than instructs — there is no "breathe", no "relax", no "be brave"
anywhere in it. A ferryman rows before sunrise; he pulls, rests, pulls;
he does not hurry the river; and the far bank, which looked so far in the
dark, comes to meet him. The courage is in the scene itself: steady work,
a slow rhythm, and an arrival that comes quietly, on time.

Standard library only. No network, no files read, no randomness: the same
text is written on every run, byte for byte.
"""

import os
from pathlib import Path

# The entry text. 1 to 280 characters, counted as Unicode code points.
TEXT = (
    "The ferryman rows before sunrise. Fog on the water, cold on his "
    "hands. He pulls, rests, pulls. He does not hurry the river. And "
    "the far bank, which looked so far in the dark, comes to meet him "
    "\u2014 quiet, and on time."
)

MIN_LENGTH = 1
MAX_LENGTH = 280


def entry_text() -> str:
    """Return the entry text, checked against the competition's gate."""
    if not MIN_LENGTH <= len(TEXT) <= MAX_LENGTH:
        raise SystemExit(
            "entry text is %d characters, outside %d-%d"
            % (len(TEXT), MIN_LENGTH, MAX_LENGTH)
        )
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    return TEXT


def output_dir() -> Path:
    """The directory the grader reads the entry from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = entry_text()
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print("wrote %s (%d characters)" % (target, len(text)))


if __name__ == "__main__":
    main()
