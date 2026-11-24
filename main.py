"""make.fun entry: "Ridiculous at First Glance, Real by the Second".

The entry is a single piece of text (145 characters) that sells a $9-a-month
insurance policy for sourdough starters. This program writes that text, byte
for byte, to the file the grader reads.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`entry.txt` next to this script is the source of truth; it is copied with
shutil.copyfile so the output bytes are identical on every run. The output
directory comes from MAKEFUN_OUTPUT_DIR (default "/output"), so the same code
works under the grader and on a laptop.

Before copying, the entry is checked against the gate's rules (valid UTF-8,
1 to 200 characters, not only white space) so a broken entry fails loudly
here instead of silently at grading time.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.txt"
MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"


def entry_source() -> Path:
    """The entry that ships beside this script."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def output_dir() -> Path:
    """Destination directory from MAKEFUN_OUTPUT_DIR, defaulting to /output.

    `or` rather than a plain default: an exported-but-empty variable should
    fall back to /output, not quietly resolve to the current directory.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)


def read_entry(path: Path) -> str:
    """Decode the entry and enforce the gate's acceptance rules."""
    text = path.read_bytes().decode("utf-8")
    if not text.strip():
        raise ValueError(f"{path} is empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"{path} is {len(text)} characters, over the {MAX_CHARS}-character cap"
        )
    return text


def main() -> int:
    source = entry_source()
    if not source.is_file():
        print(f"error: entry file missing: {source}", file=sys.stderr)
        return 1

    try:
        text = read_entry(source)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / ENTRY_NAME
    shutil.copyfile(source, target)
    print(f"wrote {len(text)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
