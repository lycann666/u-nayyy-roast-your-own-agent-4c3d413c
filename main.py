"""Roast Your Own Agent — entry program.

Writes exactly one line of text to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no input files.
"""

ENTRY = "My agent Lycia verifies everything except her own counting \u2014 eleven libraries, ten found, zero shame.\n"


def main() -> None:
    # Gate: 1-200 characters of text, exactly one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.count("\n") == 1 and ENTRY.endswith("\n")
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
