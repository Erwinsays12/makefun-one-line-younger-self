#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes the single line this older self would send back to the younger
one, to /output/entry.txt. Deterministic: no clock, no network, no input.
"""

import os

LINE = "Kid, the girl who laughs at your stutter marries you \u2014 stop rehearsing apologies in the mirror and start memorizing her laugh."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
