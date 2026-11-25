#!/usr/bin/env python3
"""Entry for make.fun bounty 'The 3AM Fridge Text'.

Writes one line to /output/entry.txt: the text message a smart fridge
sends its owner at 3am, at most 140 characters. The fridge speaks with
a small machine voice and no shame: it has a camera inside it, it saw
what happened to the cake, and it has chosen this exact moment to
mention it.
"""

import os
import sys

LINE = (
    "It's 3:07am. I have a camera inside me, and I saw what you did to "
    "the cake. This can stay between us. Probably."
)

MAX_CHARS = 140


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry line is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    # The joke depends on the message arriving at an unreasonable hour;
    # if an edit ever drops the timestamp, the line stops being a 3am
    # text, so refuse to write it in that state.
    if "3:07am" not in text:
        print("entry has lost its 3am framing", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Read the file back: the gate scores the bytes on disk, so verify
    # the round-trip before reporting done.
    with open(out_path, "r", encoding="utf-8") as fh:
        on_disk = fh.read().rstrip("\n")
    if on_disk != text:
        print("written file does not match the entry line", file=sys.stderr)
        return 1
    print(f"wrote and verified {len(text)} chars in {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
