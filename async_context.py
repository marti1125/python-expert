import asyncio
import logging
import aiosqlite
from contextlib import asynccontextmanager


@asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection()


async def get_all_users():
    async with get_connection() as conn:
        return conn.query("select ...")


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    async with aiosqlite.connect("application.db") as db:
        async with db.execute("SELECT * FROM blogs") as cursor:
            logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()