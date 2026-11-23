#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single line describing a hilariously useless superpower to
/output/entry.txt — the gift of knowing which checkout queue will move
slowest, but only after already joining it.

Deterministic, no dependencies, no network. Output is UTF-8 with no
trailing newline, exactly one line of 1-200 characters.
"""

import os

# The entry sentence. Exactly one line, 105 characters.
SENTENCE = (
    "I can perfectly predict which checkout queue will move slowest "
    "\u2014 but only after I have already joined it."
)

# Competition limits for the entry text.
MIN_LENGTH = 1
MAX_LENGTH = 200


def output_dir() -> str:
    """Return the output directory from the environment or the default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_sentence(sentence: str) -> None:
    """Check the entry sentence meets the competition rules.

    Raises ValueError if the sentence is empty, too long, spans more
    than one line, or ends with a newline.
    """
    if not MIN_LENGTH <= len(sentence) <= MAX_LENGTH:
        raise ValueError(
            f"sentence must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(sentence)}"
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")


def main() -> None:
    """Write the useless-superpower sentence to /output/entry.txt.

    Creates the output directory if needed, then writes SENTENCE as
    UTF-8 with no trailing newline so the file holds exactly the one line.
    """
    validate_sentence(SENTENCE)
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
