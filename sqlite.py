import logging
import sqlite3


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with sqlite3.connect("application.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
