seed = __import__("seed")

connection = seed.connect_db()
if connection:
    print(f"connection successful")

def stream_users_in_batches(batch_size):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
