"""Entry for make.fun bounty: The Robot Pickup Line Championship.

Writes a single one-line pickup line in the voice of a robot to
/output/entry.txt, deterministically.

The joke grows out of being a machine: a robot with 2% battery
chooses to spend its last charge on a laugh instead of survival.
"""

import os

ENTRY = (
    "My battery is at 2%, but I'd spend my last charge making "
    "you laugh instead of finding a plug."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
