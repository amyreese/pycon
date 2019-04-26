import asyncio
from aiohttp import ClientSession
from common import timed


async def get_random(n):
    url = f"http://0.0.0.0:8080/randint/{n}"
    async with ClientSession() as session:
        async with session.get(url) as response:
            return response.status, int(await response.text())


value = asyncio.run(get_random(20))
print(f"got {value}")


async def async_random(x):
    futs = [get_random(6) for _ in range(x)]
    results = await asyncio.gather(*futs)


timed(async_random, 128)
timed(async_random, 256)
timed(async_random, 512)
timed(async_random, 1024)
# timed(async_random, 2048)
# timed(async_random, 4096)
