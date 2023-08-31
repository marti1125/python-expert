import logging
import sqlite3
from typing import Generator, IO, Any
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str) -> Generator[IO[Any], None, None]:
    conn = sqlite3.connect(file_name)
    try:
        logging.info("Creating connection")
        yield conn.cursor()
    finally:
        logging.info("Closing connection")
        conn.commit()
        conn.close()


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with open_db("application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
