#!/usr/bin/env python3
"""Write one funny robot vacuum excuse for the make.fun bounty.

The entry is a single line, under 140 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = "My cliff sensor flagged your sock as a staircase, so I retreated to my dock to file a formal incident report."


def main() -> int:
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 140:
        print("entry invalid: must be one line, 1-140 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
