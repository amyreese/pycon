# Copyright 2019 John Reese
# Licensed under the MIT License

import time
from random import randint
from typing import Generator, Any, List, Iterable

from requests import get, Response

# reuse wait() from part 5
wait = __import__("5-generator-coroutines").wait

SIZE = 1024
URLS = [
    "https://2019.northbaypython.org",
    "https://duckduckgo.com",
    "https://jreese.sh",
    "https://news.ycombinator.com",
    "https://python.org",
]

def read(r: Response) -> bytes:
    data = b""
    for chunk in r.iter_content(SIZE):
        data += chunk
        yield
    return data

def fetch(url: str) -> str:
    with get(url, stream=True) as r:
        data = yield from read(r)
    return data.decode("utf-8")

def main():
    coros = [fetch(url) for url in URLS]
    results = wait(coros)
    for result in results:
        print(f"{result[:20]!r}")


if __name__ == "__main__":
    main()
