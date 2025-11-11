import pyodbc
from seed import connect_db


def stream_user_ages():
    """
    Generator that yields ages one by one
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data;")  # Only fetch age column

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row[0]  # only the age

    cursor.close()
    conn.close()


def compute_average_age():
    """
    Computes average age using the stream_user_ages generator
    (no SQL AVG, must use <= 2 loops)
    """
    total = 0
    count = 0

    # Loop #1 – reading ages
    for age in stream_user_ages():
        total += age
        count += 1

    # No loop here – just math
    average = total / count if count > 0 else 0

    print(f"Average age of users: {average}")
    return average


if __name__ == "__main__":
    compute_average_age()
