#!/usr/bin/python3
"""Translator Assembly to Machine Code"""

import sys


def get_asm_token(line):
    return line.split(";", 1)[0].strip()


def translate(lines):
    return


def main(source, target):
    with open(source, encoding="utf-8") as f:
        lines = f.readlines()

    code = translate(lines)


if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python translator.py <input_file> <output_file>"
    name, source, target = sys.argv[0], sys.argv[1], sys.argv[2]
    main(source, target)
