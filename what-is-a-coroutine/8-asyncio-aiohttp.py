# Copyright 2019 John Reese
# Licensed under the MIT License

import asyncio
import time

from aiohttp import request

URLS = [
    "https://2019.northbaypython.org",
    "https://duckduckgo.com",
    "https://jreese.sh",
    "https://news.ycombinator.com",
    "https://python.org",
]

# Coroutines with aiohttp


async def fetch(url: str) -> str:
    async with request("GET", url) as r:
        return await r.text("utf-8")


async def main():
    coros = [fetch(url) for url in URLS]
    results = await asyncio.gather(*coros)
    for result in results:
        print(f"{result[:20]!r}")


if __name__ == "__main__":
    asyncio.run(main())
