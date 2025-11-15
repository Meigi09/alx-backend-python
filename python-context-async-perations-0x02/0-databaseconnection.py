#!/usr/bin/env python3
import sqlite3


class DatabaseConnection:
    """Custom class-based context manager for DB connection."""

    def __init__(self, db_name="users.db"):
        """Store the database name."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """Open the database connection and return the cursor."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the connection automatically."""
        if self.conn:
            self.conn.close()
        # do not suppress exceptions
        return False


# Using the context manager to run SELECT * FROM users
if __name__ == "__main__":
    with DatabaseConnection() as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)
