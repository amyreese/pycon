import asyncio
import contextlib
import aiosqlite

DB = "pycon.db"


class MessageContext:
    def __init__(self, sender):
        self.sender = sender
        self.db = None

    async def __aenter__(self):
        self.db = await aiosqlite.connect(DB)
        await self.init_schema()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.db:
            await self.db.commit()
            await self.db.close()

    async def init_schema(self):
        query = """
            CREATE TABLE IF NOT EXISTS messages
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                recipient TEXT,
                message TEXT
            )
        """
        await self.db.execute(query)

    async def send(self, recipient, message):
        query = """
            INSERT INTO messages (sender, recipient, message)
            VALUES (?, ?, ?)
        """
        params = (self.sender, recipient, message)
        async with self.db.execute(query, params) as cursor:
            return cursor.lastrowid


async def main():
    async with MessageContext("Jack") as ctx:
        await ctx.send("Jill", "I'm out of water")
        await ctx.send("Terry", "Do you know where my pail is?")


asyncio.run(main())


@contextlib.asynccontextmanager
async def db_commit():
    async with aiosqlite.connect(DB) as db:
        yield db
        await db.commit()


async def main():
    async with db_commit() as db:
        query = """
            INSERT INTO messages (sender, recipient, message)
            VALUES (?, ?, ?)
        """
        await db.execute(query, ("Bacon", "Hobbes", "Let's go exploring!"))

    query = "SELECT * FROM messages"
    async with aiosqlite.connect(DB) as db:
        async with db.execute(query) as cursor:
            async for row in cursor:
                rowid, sender, recipient, message = row
                print(f"row #{rowid} from {sender} to {recipient}: {message}")


asyncio.run(main())
