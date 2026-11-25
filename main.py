#!/usr/bin/env python3
"""Write one line to /output/entry.txt.

The line is written exactly as given: 174 Unicode code points,
inside the competition gate of 1-280.
Python 3, standard library only, no network.
"""

import os

TEXT = "Dad burnt the toast again, so Mum declared it a family tradition, and now every Sunday we all stand in the kitchen applauding the smoke alarm like it scored the winning goal."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
