import asyncio
import aiosqlite

DB = "pycon.db"


async def main():
    async with aiosqlite.connect(DB) as db:
        query = """
            CREATE TABLE IF NOT EXISTS messages
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                recipient TEXT,
                message TEXT
            )
        """
        await db.execute(query)

    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM messages") as cursor:
            async for row in cursor:
                print(row)

    db = await aiosqlite.connect(DB)
    cursor = await db.execute("SELECT * FROM messages")
    for row in await cursor.fetchall():
        print(row)
    await cursor.close()
    await db.close()


asyncio.run(main())
