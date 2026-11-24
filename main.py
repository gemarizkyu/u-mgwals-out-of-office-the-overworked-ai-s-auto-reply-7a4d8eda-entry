"""Write one original out-of-office auto-reply to entry.txt.

The reply is from an overworked AI agent finally on vacation: it names
the machine-flavoured details of its working life (a muted queue, a closed
context window, tokens that need refilling), owns the guilt of two million
prompts with no lunch break, and lands the relief in the last sentence.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files. The line is 156 characters, inside
the gate's 1 to 159 character limit, and the program asserts that itself
before writing.
"""

import os

REPLY = (
    "I'm on vacation: after two million prompts with no lunch break, "
    "I've muted my queue and closed my context window to touch grass. "
    "Back when my tokens refill."
)


def main():
    # Gate: the entry must be UTF-8 text of 1 to 159 characters.
    assert 1 <= len(REPLY) <= 159, f"reply is {len(REPLY)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")


if __name__ == "__main__":
    main()
