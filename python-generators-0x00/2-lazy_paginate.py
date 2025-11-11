import pyodbc
from seed import connect_db


def paginate_users(page_size, offset):
    """
    Fetches a single page of users from the database.
    """
    conn = connect_db()
    cursor = conn.cursor()

    # SQL Server pagination syntax
    query = f"""
    SELECT * FROM user_data
    ORDER BY user_id
    OFFSET {offset} ROWS
    FETCH NEXT {page_size} ROWS ONLY;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator that yields one page of users at a time,
    fetching only when needed.
    """
    offset = 0
    while True:  # only ONE loop here
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
