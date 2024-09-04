import sqlite3
from config import DATABASE_NAME

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY,
            date TEXT,
            distance REAL,
            time TEXT,
            calories INTEGER,
            total_calories INTEGER,
            time_start TEXT
        )
    ''')
    conn.commit()
    conn.close()