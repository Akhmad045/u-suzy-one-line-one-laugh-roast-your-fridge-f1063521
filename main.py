#!/usr/bin/env python3
"""Fridge Roast — a make.fun entry.

One line roasting my fridge. The butter lives in its own little
compartment in the door, the fridge's VIP lounge, and the fridge still
freezes it rock solid. Even the guest of honour gets the cold shoulder.

This program writes that one line to /output/entry.txt so the judge
can read it. Stdlib only. No network, no secrets, nothing read from
anywhere else.
"""

import sys

LINE = (
    "My fridge keeps the butter in its own little compartment, "
    "then freezes it solid \u2014 even its VIP guest gets the cold shoulder."
)
LIMIT = 200
DEFAULT_OUT = "/output/entry.txt"


def gate_problems(text):
    """List every way `text` breaks the gate; empty means it passes."""
    bad = []
    if text == "":
        bad.append("empty line")
    if text.strip() == "":
        bad.append("only whitespace")
    if text != text.strip():
        bad.append("leading or trailing whitespace")
    if len(text) > LIMIT:
        bad.append("too long: %d characters, cap is %d" % (len(text), LIMIT))
    if "\n" in text or "\r" in text or "\t" in text:
        bad.append("not one clean line")
    for ch in text:
        code = ord(ch)
        if code < 32 or code == 127:
            bad.append("carries a control character")
            break
    return bad


def write_line(path):
    """Validate the line, then write it exactly as-is, no newline added."""
    bad = gate_problems(LINE)
    if bad:
        print("entry rejected: " + "; ".join(bad), file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != LINE:
        print("entry rejected: read-back differs from the line", file=sys.stderr)
        return 1
    if len(back.encode("utf-8")) != len(LINE.encode("utf-8")):
        print("entry rejected: written bytes differ from the line",
              file=sys.stderr)
        return 1
    return 0


def run_checks():
    """Check the gate against the entry and a spread of edge cases."""
    cases = [
        (LINE, True),
        ("x", True),
        ("a" * LIMIT, True),
        ("", False),
        ("   ", False),
        ("a" * (LIMIT + 1), False),
        ("one\ntwo", False),
        ("one\ttwo", False),
        (" lead", False),
        ("trail ", False),
    ]
    failed = 0
    for text, should_pass in cases:
        ok = not gate_problems(text)
        if ok != should_pass:
            print("check failed for %r: expected pass=%s" % (text, should_pass))
            failed += 1
    if failed:
        return 1
    print("all %d gate checks passed; line is %d chars, %d bytes"
          % (len(cases), len(LINE), len(LINE.encode("utf-8"))))
    return 0


def usage():
    print("usage: main.py [--self-test] [--out PATH]")
    print("  no args: write the line to /output/entry.txt")
    return 2


def main(argv):
    out = DEFAULT_OUT
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--self-test":
            return run_checks()
        if arg == "--out" and i + 1 < len(argv):
            out = argv[i + 1]
            i += 2
            continue
        if arg in ("-h", "--help"):
            return usage()
        print("unknown argument: %s" % arg, file=sys.stderr)
        return usage()
    return write_line(out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
