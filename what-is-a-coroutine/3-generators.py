# Copyright 2019 John Reese
# Licensed under the MIT License

import time
from random import randint
from typing import Generator, Any, List, Iterable

NoResult = object()

## Generator Basics

def fib(count: int):
    a, b = 1, 0
    for _ in range(count):
        a, b = b, a + b
        yield b

def main():
    gen = fib(5)
    print(gen)
    while True:
        print(next(gen))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e=}")

