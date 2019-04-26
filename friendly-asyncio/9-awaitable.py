import asyncio
from aiohttp import ClientSession


class Random:
    def __init__(self, limit):
        self.limit = limit

    async def get(self):
        url = f"http://0.0.0.0:8080/randint/{self.limit}"
        async with ClientSession() as session:
            async with session.get(url) as response:
                return int(await response.text())

    def __await__(self):
        return self.get().__await__()


async def main():
    random = Random(50)
    print(await random)
    print(await random)


asyncio.run(main())


class MultiRandom:
    def __init__(self, limit, count):
        self.random = Random(limit)
        self.count = count

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count <= 0:
            raise StopAsyncIteration()
        self.count -= 1
        return await self.random


async def main():
    async for value in MultiRandom(20, 5):
        print(value)

    values = [v async for v in MultiRandom(40, 3)]
    print(values)


asyncio.run(main())


async def multi_random(limit, count):
    random = Random(limit)
    futures = [asyncio.create_task(random.get()) for _ in range(count)]
    for future in futures:
        yield await future


async def main():
    async for value in multi_random(20, 3):
        print(value)


asyncio.run(main())
