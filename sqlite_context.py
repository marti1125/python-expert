import logging
import sqlite3
from typing import Any


class SQLite:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)
    
    def __enter__(self) -> Any:
        logging.info("Calling __enter__")
        return self.connection.cursor()


    def __exit__(self, error: Exception, value: object, traceback: object) -> None:
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with SQLite("application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
