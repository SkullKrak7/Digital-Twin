import sqlite3
import pandas as pd

def fetch_sensor_data():
    """Fetches the last 5 records from the sensor database and displays them."""
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sensors ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()

    conn.close()

    df = pd.DataFrame(rows, columns=["id", "timestamp", "temperature","vibration","pressure"])
    print(df)

if __name__ == "__main__":
    fetch_sensor_data()