import asyncio
from common import timed


async def get_random(n):
    r, w = await asyncio.open_connection("::1", 8080)
    w.write(f"{n}\n".encode("utf-8"))
    await w.drain()
    resp = await r.readline()
    value = int(resp.decode("utf-8").strip())
    w.close()
    return value


timed(get_random, 20)


async def async_random(x):
    futs = [get_random(6) for _ in range(x)]
    results = await asyncio.gather(*futs)


timed(async_random, 128)
timed(async_random, 256)
timed(async_random, 512)
timed(async_random, 1024)
# timed(async_random, 2048)
# timed(async_random, 4096)
