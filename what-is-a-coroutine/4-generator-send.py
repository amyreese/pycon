# Copyright 2022 Amethyst Reese
# Licensed under the MIT License

import time
from random import randint
from typing import Generator, Any, List, Iterable

NoResult = object()

## Sending values into generators

def counter(start = 0, limit = 10):
    value = start
    while value < limit:
        value += yield value
    yield value
    
def main():
    gen = counter()
    gen.send(None)  # prime the generator
    while True:
        value = randint(1, 3)
        total = gen.send(value)
        print(f"sent {value}, got {total}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
