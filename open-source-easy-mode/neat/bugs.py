# Copyright 2022 John Reese
# Licensed under the MIT License

# THIS CODE IS INTENTIONALLY AWFUL
# flake8: noqa
# type: ignore

from pathlib import Path
from typing import List, NewType, Optional

ID = NewType("ID", int)
Record = NewType("Record", dict)


def create_record(id, value):
    ...


def create_record(id: ID, value: str) -> Record:
    ...


def get_path(key):
    ...


def subtle_bug(key):
    path = get_path(key)
    with open(path) as f:
        ...


def get_path(key: str) -> Optional[Path]:
    ...


def subtle_bug(key: str) -> None:
    path = get_path(key)
    with open(path) as f:
        ...


def get_path(key: str) -> Optional[Path]:
    ...


def subtle_bug(key: str) -> None:
    path: Optional[Path] = get_path(key)
    with open(path) as f:
        ...
