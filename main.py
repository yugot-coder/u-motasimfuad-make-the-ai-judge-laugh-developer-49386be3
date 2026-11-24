"""Make the AI Judge Laugh: Developer Excuses.

One funny single-line excuse a developer gives when code breaks in
production, at most 200 characters.

Standard library only. Deterministic: no randomness, no network, no
clock. Writes the line to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt).
"""

import os

LINE = "It works on my machine, so I shipped my machine — prod is now my laptop, which is why the site goes down when I close the lid."


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        read_back = f.read()
    if read_back != line + "\n":
        raise SystemExit(f"read-back mismatch: wrote {line!r}, read {read_back!r}")
    print(line)


if __name__ == "__main__":
    main()
