import sqlite3
from datetime import datetime

class ConversationDB:
    def __init__(self, db_path="conversations.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT NOT NULL,
                    message TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    session_id TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_message(self, role, message, session_id):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO conversations (role, message, session_id) VALUES (?, ?, ?)",
                (role, message, session_id)
            )
            conn.commit()

    def get_session_messages(self, session_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT role, message FROM conversations WHERE session_id = ? ORDER BY timestamp",
                (session_id,)
            )
            return cursor.fetchall()

    def clear_old_sessions(self, days=7):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                f"DELETE FROM conversations WHERE timestamp < datetime('now', '-{days} days')"
            )
            conn.commit()
