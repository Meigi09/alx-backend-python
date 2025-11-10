import pyodbc

def connect_db():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost,1433;'
    'DATABASE=ALX_prodev;'
    'Trusted_Connection=yes;'
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("IF DB_ID('ALX_prodev') IS NULL CREATE DATABASE ALX_prodev;")
    cursor.commit()
    cursor.close()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        IF OBJECT_ID('user_data', 'U') IS NULL
        CREATE TABLE user_data (
            user_id UNIQUEIDENTIFIER PRIMARY KEY,
            name NVARCHAR(255) NOT NULL,
            email NVARCHAR(255) NOT NULL,
            age INT NOT NULL
        );
    """)
    cursor.commit()
    cursor.close()


if __name__ == "__main__":
    conn = connect_db()
    create_database(conn)
    create_table(conn)
    conn.close()
    print("✅ Database ALX_prodev is ready.")
