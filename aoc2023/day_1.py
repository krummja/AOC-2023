from __future__ import annotations
from pathlib import Path
import os

SRCDIR = Path(os.getcwd())
INPUTS = Path(SRCDIR, "inputs")


sample_inputs = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


def parse_calibration_value(strvalue: str) -> int:
    digits = []
    for char in strvalue:
        if char.isalpha():
            continue
        digits.append(char)

    if len(digits) == 1:
        return int(digits[0] + digits[0])

    first = digits[0]
    last = digits[-1]
    return int(first + last)


def parse_calibration_values(inputs: list[str]) -> list[int]:
    values = []
    for value in inputs:
        values.append(parse_calibration_value(value))
    return values


def main() -> None:
    with open(Path(INPUTS, "day_1.txt"), "r") as file:
        inputs = [line.rstrip("\n") for line in file]
        values = parse_calibration_values(inputs)
        print(sum(values))


if __name__ == '__main__':
    main()
