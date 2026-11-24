"""Write a single sunrise emoji as a dream-vacation entry.

This program creates the make.fun entry file and fills it with
exactly one emoji: a sunrise over the ocean, chosen as the whole
dream vacation in a single picture. Nothing else is written, so
the file stays at one character and four UTF-8 bytes every run.
"""

import os
from pathlib import Path

EMOJI = "🌅"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def resolve_output_dir() -> Path:
    """Return the directory that should hold the entry file."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_bytes(EMOJI.encode("utf-8"))


if __name__ == "__main__":
    main()
