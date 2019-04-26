import asyncio


async def foo():
    print("running foo")
    return 1


async def bar():
    coro = foo()
    print(f"got coroutine: {coro}")
    value = await coro
    print(f"got {value} from coroutine")


asyncio.run(bar())


async def nap(n):
    coro = asyncio.sleep(n)
    print(f"coro: {coro}")
    task = asyncio.create_task(coro)
    print(f"task: {task}")
    await asyncio.sleep(n + 1)
    print(f"task: {task}")
    await task


# asyncio.run(nap(2))


async def get_random(n=20):
    r, w = await asyncio.open_connection("::1", 8080)
    w.write(f"{n}\n".encode("utf-8"))
    await w.drain()
    resp = await r.readline()
    value = int(resp.decode("utf-8").strip())
    w.close()
    return value


async def main():
    values = await asyncio.gather(get_random(), get_random())
    print(f"gather two: {values}")
    futures = [random() for _ in range(10)]
    values = await asyncio.gather(*futures)
    print(f"gather ten: {values}")


asyncio.run(main())

