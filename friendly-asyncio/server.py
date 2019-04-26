import asyncio
import uvloop
from random import randint

# uvloop.install()


async def serve_randint(reader, writer):
    request = (await reader.readline()).decode("utf-8").strip()
    try:
        limit = int(request)
        print(f"received request: {request}")
    except ValueError:
        print(f"unknown value: {request}")
        limit = 20

    await asyncio.sleep(0.1)  # thinking

    value = randint(0, limit)
    writer.write(f"{value}\n".encode("utf-8"))
    writer.close()


async def main(port=8080):
    server = await asyncio.start_server(serve_randint, host="::1", port=port)
    async with server:
        print(f"listening on {port}...")
        await server.serve_forever()


asyncio.run(main())
