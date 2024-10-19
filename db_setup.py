import sqlite3

def create_connection():
    conn = sqlite3.connect('rules.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Define schema for storing rules
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def insert_rule(rule_string):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Insert a rule into the database
    cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (rule_string,))
    conn.commit()
    conn.close()
