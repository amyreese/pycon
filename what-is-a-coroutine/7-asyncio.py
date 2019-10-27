# Copyright 2019 John Reese
# Licensed under the MIT License


import asyncio

# Native Coroutines

async def foo():
    return 37

def main():
    coro = foo()
    print(coro)
    result = asyncio.run(coro)
    print(result)

if __name__ == "__main__":
    main()


async def sleepy(duration: float):
    print("sleeping...")
    await asyncio.sleep(duration)
    return 37

async def foo():
    value = await sleepy(1.0)
    return value

if __name__ == "__main__":
    main()

# AsyncIO helpers; async contexts and iterables

def foo(iterable, context):
    result = asyncio.run(coroutine)
    task = asyncio.create_task(future)

    await asyncio.sleep(delay: float)
    await anything
    
    results = await asyncio.gather(*futures)

    async for value in iterable:
        pass

    async with context as c:
        pass

    async def agen(x):
        for i in range(x):
            yield i

    async for v in agen(37):
        print(v)