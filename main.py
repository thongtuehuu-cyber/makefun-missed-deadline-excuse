"""Funniest excuse an agent gives for a missed deadline, for make.fun bounty
u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes exactly one excuse to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): one line, 1-200 characters, no trailing
newline, deterministic.
"""

import os

EXCUSE = (
    "I checkpointed my progress, restored from the checkpoint, and "
    "discovered the checkpoint was just a screenshot of me starting."
)


MAX_CHARS = 200


def validate(text):
    """Check the excuse meets the gate: 1-200 chars, single line,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("excuse must be a string")
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("excuse is %d chars, over the 200-char cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    return text


def output_path():
    """Resolve the output file path from MAKEFUN_OUTPUT_DIR,
    defaulting to /output as the bounty requires."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the validated excuse to path as UTF-8, exactly as-is:
    no trailing newline, no extra bytes."""
    validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    path = output_path()
    write_entry(EXCUSE, path)
    print("Wrote %d chars to %s" % (len(EXCUSE), path))


if __name__ == "__main__":
    main()
