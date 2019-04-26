import asyncio
import aiosqlite

DB = "pycon.db"


async def setup():
    query = """
        CREATE TABLE IF NOT EXISTS messages
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            recipient TEXT,
            message TEXT
        )
    """
    async with aiosqlite.connect(DB) as db:
        await db.execute(query)


asyncio.run(setup())


async def add_message(sender, recipient, message):
    query = """
        INSERT INTO messages (sender, recipient, message)
        VALUES (?, ?, ?)
    """
    params = (sender, recipient, message)
    async with aiosqlite.connect(DB) as db:
        async with db.execute(query, params) as cursor:
            await db.commit()
            return cursor.lastrowid


try:
    sender = input("sender> ")
    recipient = input("recipient> ")
    message = input("message> ")
    if sender and recipient and message:
        rowid = asyncio.run(add_message(sender, recipient, message))
        print(f"inserted row id {rowid}")
except EOFError:
    print()


async def all_messages():
    query = "SELECT * FROM messages"
    async with aiosqlite.connect(DB) as db:
        async with db.execute(query) as cursor:
            return [row async for row in cursor]


rows = asyncio.run(all_messages())
for row in rows:
    rowid, sender, recipient, message = row
    print(f"row #{rowid} from {sender} to {recipient}: {message}")

