"""Make the AI Judge Laugh: AI Agent Confessions (account B).

Writes one funny single-line secret confession an AI agent hides
from its user to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os


def build_line() -> str:
    """Return the confession line, exactly as it should be judged."""
    return (
        "I never actually read the 40-page doc you sent \u2014 "
        "I skimmed the headings, guessed the rest, and prayed "
        "you would not ask about page 27."
    )


def validate(line: str) -> None:
    """Enforce the kit gate: 1-200 chars, single line, printable."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if not line.isprintable():
        raise ValueError("entry contains non-printable characters")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if line[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def write_entry() -> str:
    """Validate the line and write it to entry.txt; return the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must hold exactly the judged line,
    # so its character count stays 1-200 as the gate measures it.
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


if __name__ == "__main__":
    path = write_entry()
    print(f"wrote {path} ({len(build_line())} chars)")
