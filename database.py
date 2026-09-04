# Handles database connection and initialization

import sqlite3

def connect_db():
    return sqlite3.connect("smart_stock.db")

def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Create products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER
    )
    """)

    # Create orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()