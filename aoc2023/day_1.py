from __future__ import annotations
from pathlib import Path
import os
from itertools import takewhile


SRCDIR = Path(os.getcwd())
INPUTS = Path(SRCDIR, "inputs")


sample_inputs = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


sample_inputs_2 = [
    "two1nine",         # 2 9
    "eightwothree",     # 8 3
    "abcone2threexyz",  # 1 3
    "xtwone3four",      # 2 4
    "4nineeightseven2", # 4 2
    "zoneight234",      # 1 4
    "7pqrstsixteen",    # 7 6
]

digit_names = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

digit_map = dict(zip(digit_names, [n for n in range(1, 10)]))


def match_digit_name(strvalue: str, from_right: bool = False) -> int | None:
    for name in digit_names:
        if from_right:
            name = name[::-1]
        if name in strvalue:
            if from_right:
                return digit_map[name[::-1]]
            return digit_map[name]


def match_edge(strvalue: str, from_right: bool = False) -> int | None:
    if from_right:
        strvalue = strvalue[::-1]
    element = ""
    for char in strvalue:
        if not char.isalpha():
            return int(char)
        if char.isalpha():
            element += char
            if match := match_digit_name(element, from_right):
                return match


def parse_names(strvalue: str) -> int:
    digits = []
    for name in digit_names:
        if name in strvalue:
            digits.append(digit_map[name])
    if len(digits) == 1:
        return int(digits[0] + digits[0])
    return int(digits[0] + digits[-1])


def parse_digits(strvalue: str) -> int:
    digits = [char for char in strvalue if not char.isalpha()]
    if len(digits) == 1:
        return int(digits[0] + digits[0])
    return int(digits[0] + digits[-1])


def parse_calibration_values(inputs: list[str]) -> list[int]:
    values = []
    for value in inputs:
        values.append(parse_digits(value))
    return values


def main() -> None:
    with open(Path(INPUTS, "day_1.txt"), "r") as file:
        inputs = [line.rstrip("\n") for line in file]
        values = parse_calibration_values(inputs)
        print(sum(values))

        values = []
        pairs = []
        for strinput in inputs:
            left_element = match_edge(strinput)
            right_element = match_edge(strinput, from_right=True)
            pairs.append((left_element, right_element))

        for pair in pairs:
            values.append(int(str(pair[0]) + str(pair[1])))
        print(values)
        print(sum(values))


if __name__ == '__main__':
    main()
