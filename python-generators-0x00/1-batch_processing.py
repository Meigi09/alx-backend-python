import pyodbc
from seed import connect_db  # reuse your working connection


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of rows from user_data.
    Each batch is a list of tuples.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data;")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch  # give out one batch
            batch = []  # reset for next batch

    if batch:  # if there are leftovers smaller than batch_size
        yield batch

    cursor.close()
    conn.close()


def batch_processing(batch_size):
    """
    Processes batches of users and yields only users older than 25.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user[3] > 25]  # age is 4th column
        yield filtered
