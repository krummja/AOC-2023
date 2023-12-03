from __future__ import annotations
from load import load_input


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


def match_digit_name(strvalue: str) -> int | None:
    for name in digit_names:
        if name in strvalue:
            return digit_map[name]


def match_digit_name_reverse(strvalue: str) -> int | None:
    for name in digit_names:
        name = name[::-1]
        if name in strvalue:
            return digit_map[name[::-1]]


def match_left_edge(strvalue: str) -> int | None:
    element = ""
    for char in strvalue:
        if not char.isalpha():
            return int(char)
        if char.isalpha():
            element += char
            if match := match_digit_name(element):
                return match


def match_right_edge(strvalue: str) -> int | None:
    element = ""
    for char in strvalue[::-1]:
        if not char.isalpha():
            return int(char)
        if char.isalpha():
            element += char
            if match := match_digit_name_reverse(element):
                return match


def parse_calibration_values_two(inputs: list[str]) -> list[int]:
        values = []
        pairs = []
        for strinput in inputs:
            left_element = match_left_edge(strinput)
            right_element = match_right_edge(strinput)
            pairs.append((left_element, right_element))

        for pair in pairs:
            values.append(int(str(pair[0]) + str(pair[1])))
        return values


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


def parse_calibration_values_one(inputs: list[str]) -> list[int]:
    values = []
    for value in inputs:
        values.append(parse_digits(value))
    return values


def main() -> None:
    with load_input(1) as file:
        inputs = [line.rstrip("\n") for line in file]

        # Part One
        values = parse_calibration_values_one(inputs)
        print(sum(values))

        # Part Two
        values = parse_calibration_values_two(inputs)
        print(sum(values))


if __name__ == '__main__':
    main()
