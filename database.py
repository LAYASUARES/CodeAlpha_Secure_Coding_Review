import sqlite3

# Hardcoded credentials (Vulnerability)
DB_USER = "admin"
DB_PASSWORD = "123456"

def get_connection():
    return sqlite3.connect("users.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_user(username, email):
    # SQL Injection Vulnerability
    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def search_user(term):
    # Vulnerable to SQL Injection
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username LIKE '%{term}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
