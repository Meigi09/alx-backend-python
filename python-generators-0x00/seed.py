import csv
import uuid

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = str(uuid.uuid4())
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (?, ?, ?, ?)
            """, (user_id, row['name'], row['email'], int(row['age'])))
    
    cursor.commit()
    cursor.close()
