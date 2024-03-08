# BaseTable.py

# This file contains the base class for all tables in the database.

import sqlite3


class BaseTable:
    """
    Represents a base table in the Messie Jessie database.

    Attributes:
        db_name (str): The name of the SQLite database.
        conn (sqlite3.Connection): The connection to the database.
        cursor (sqlite3.Cursor): The cursor object for executing SQL statements.

    Methods:
        connect(): Connects to the SQLite database.
        disconnect(): Disconnects from the SQLite database.
    """

    def __init__(self, db_name="MessieJessie.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        Connects to the SQLite database.

        Raises:
            MyDatabaseConnectionError: If there is an error connecting to the database.
            MyGeneralError: If an unexpected error occurs.

        Returns:
            None
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            raise MyDatabaseConnectionError("Error connecting to the database") from e
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise MyGeneralError("An unexpected error occurred") from e

    def disconnect(self):
        """
        Disconnects from the SQLite database.

        Returns:
            None
        """
        try:
            if self.conn:
                self.conn.close()
                print("Database disconnected successfully!")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")


# Add custom exception classes here if needed
class MyDatabaseConnectionError(Exception):
    pass


class MyGeneralError(Exception):
    pass
