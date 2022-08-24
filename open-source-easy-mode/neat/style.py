# Copyright 2022 Amethyst Reese
# Licensed under the MIT License

import re
from pathlib import Path
from typing import List, Optional

import click
from attr import dataclass

from .data import VALUE

SOME_REGEX = re.compile(r"(\w)(\w)(\w)\3\2\1")


class object:
    def first_method(self, path: Path) -> "object":
        return self

    def second_method(self, items: List[str]) -> "object":
        return self

    def third_method(self, return_exceptions: Optional[bool]) -> List[str]:
        return []


def example_function(
    argument_one: List[str],
    argument_two: Optional[bool] = False,
) -> List[str]:
    path = Path("something")
    result = (
        object()
        .first_method(path)
        .second_method(items=argument_one)
        .third_method(return_exceptions=argument_two)
    )

    return result


def use_names() -> None:
    # act like we're using stuff we imported
    print(click, dataclass, VALUE)
