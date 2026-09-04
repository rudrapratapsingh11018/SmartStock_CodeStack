# Inserts sample data into database

from database import connect_db

def seed():
    conn = connect_db()
    cursor = conn.cursor()

    products = [
        ("Rice", 50),
        ("Wheat", 30),
        ("Sugar", 20)
    ]

    cursor.executemany("INSERT INTO products (name, quantity) VALUES (?, ?)", products)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()