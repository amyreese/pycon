import asyncio
import time


async def hungry():
    print("getting food")
    before = time.time()
    await asyncio.sleep(0.1)
    duration = time.time() - before
    print(f"full now, took {duration:.1f}s")


asyncio.run(hungry())


async def nap():
    print("nap time")
    time.sleep(2)
    print("nap over")


async def main():
    await asyncio.gather(hungry(), nap())


asyncio.run(main())


async def nap2():
    loop = asyncio.get_running_loop()
    print("nap time")
    await loop.run_in_executor(None, time.sleep, 2)
    print("nap over")


async def main():
    await asyncio.gather(hungry(), nap2())


asyncio.run(main())


async def count(x):
    return x


async def counting(k, x):
    print(f"{k}: counting to {x}")
    for _ in range(x):
        await count(x)
    print(f"{k}: ... {x-1} ... {x}")


async def main():
    coros = [counting(k, 100_000) for k in range(5)]
    tasks = [asyncio.create_task(c) for c in coros]

    await asyncio.gather(*tasks)


asyncio.run(main())


async def count(x):
    await asyncio.sleep(0)
    return x


async def counting(k, x):
    print(f"{k}: counting to {x}")
    for _ in range(x):
        await count(x)
    print(f"{k}: ... {x-1} ... {x}")


async def main():
    coros = [counting(k, 100_000) for k in range(4)]
    tasks = [asyncio.create_task(c) for c in coros]

    await asyncio.gather(*tasks)


asyncio.run(main())
