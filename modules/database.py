# powerd by @kingproject24

from database import Database

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT
            );
        """)
        self.conn.commit()

    def insert_user(self, id, username):
        self.cursor.execute("INSERT INTO users (id, username) VALUES (?, ?)", (id, username))
        self.conn.commit()

    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()

import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT
            );
        """)
        self.conn.commit()

    def insert_user(self, id, username):
        self.cursor.execute("INSERT INTO users (id, username) VALUES (?, ?)", (id, username))
        self.conn.commit()

    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()
