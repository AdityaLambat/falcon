import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


class DatabaseConnection:

    def __init__(self):

        self.connection = psycopg2.connect(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD")
        )

    def get_connection(self):

        return self.connection

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def close(self):

        if self.connection:
            self.connection.close()