seed = __import__("seed")

connection = seed.connect_db()
if connection:
    print(f"connection successful")


def stream_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")  # fetch all rows

    while True:
        row = cursor.fetchone()  # get one row at a time
        if row is None:
            break
        yield row

    cursor.close()
    connection.close()

if __name__ == "__main__":
    for user in stream_users():
        print(user)
