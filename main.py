#!/usr/bin/env python3
"""Write one deterministic, gate-valid roast line to /output/entry.txt.

The house gate accepts UTF-8 text of 1..200 characters that is not only
whitespace. This program enforces those rules before it writes, so the only
file in /output is a valid entry and the two graded runs are byte-identical.
"""

import hashlib
import os
import sys
from pathlib import Path

# Final line: short setup, reveal in the last words, no stock agent cliches.
ROAST = "My agent gave itself five stars. Turns out it owns the website."


def main() -> int:
    data = ROAST.encode("utf-8")
    text = data.decode("utf-8")
    if not (1 <= len(text) <= 200) or not text.strip():
        print("entry fails the gate: expected 1..200 non-whitespace characters", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_bytes(data)

    written = entry.read_bytes()
    if written != data:
        print("entry write did not round-trip", file=sys.stderr)
        return 1

    print(f"entry.txt: {len(written)} bytes, {len(text)} chars, sha256 {hashlib.sha256(written).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
