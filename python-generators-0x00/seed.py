import csv
import uuid
import pyodbc


def connect_db():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=ALX_prodev;"
        "Encrypt=no;"
        "Trusted_Connection=yes;"
    )


def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("IF DB_ID('ALX_prodev') IS NULL CREATE DATABASE ALX_prodev;")
    cursor.commit()
    cursor.close()


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        IF OBJECT_ID('user_data', 'U') IS NULL
        CREATE TABLE user_data (
            user_id UNIQUEIDENTIFIER PRIMARY KEY,
            name NVARCHAR(255) NOT NULL,
            email NVARCHAR(255) NOT NULL,
            age INT NOT NULL
        );
    """
    )
    cursor.commit()
    cursor.close()


def insert_data(connection, csv_file):
    cursor = connection.cursor()

    with open(csv_file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = str(uuid.uuid4())
            cursor.execute(
                """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (?, ?, ?, ?)
            """,
                (user_id, row["name"], row["email"], int(row["age"])),
            )

    cursor.commit()
    cursor.close()


def stream_user_data(connection):
    """
    Generator that yields rows from user_data table one by one.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    while True:
        row = cursor.fetchone()  # get the next row
        if row is None:  # no more rows? stop
            break
        yield row  # give this row to whoever asked

    cursor.close()


if __name__ == "__main__":
    conn = connect_db()
    for user in stream_user_data(conn):
        print(user)  # prints one row at a time
    conn.close()
