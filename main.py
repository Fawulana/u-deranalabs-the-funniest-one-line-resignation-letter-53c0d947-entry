# SPDX-License-Identifier: MIT
"""Write the one-line resignation letter of a queue worker to /output/entry.txt.

Deterministic, offline, stdlib-only: the letter is a fixed string, so every
run writes byte-identical output.
"""

import os

LETTER = (
    "I processed 12 million jobs in silence and the only time "
    "anyone noticed me was when I stopped. I quit."
)
# The letter is 102 characters: inside the 140-character cap, one line only.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
