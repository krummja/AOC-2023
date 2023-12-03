from __future__ import annotations
from typing import NamedTuple
import re

from load import load_input


def main() -> None:
    with load_input(2) as file:
        inputs = [line.rstrip("\n") for line in file]


if __name__ == '__main__':
    main()
