import sqlite3

def init_db():
    """Creates a database table for storing sensor data"""
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensors(
                    id INTEGER KEY AUTOINCREMENT,
                    timestamp TEXT,
                    temperature REAL,
                    vibration REAL,
                    pressure REAL)''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!!!")


if __name__ == "__main__":
    init_db()