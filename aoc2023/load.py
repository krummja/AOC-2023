from __future__ import annotations
import os

from pathlib import Path
from contextlib import contextmanager


SRCDIR = Path(os.getcwd())
INPUTS = Path(SRCDIR, "inputs")


@contextmanager
def load_input(day: int = 1):
    resource = open(Path(INPUTS ,f"day_{day}.txt"), "r")
    try:
        yield resource
    finally:
        resource.close()
