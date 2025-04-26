import sqlite3
from scripts.data_gen import generate_sensor_data

def store_sensor_data(data):
    """Reads sensor data from CSV and stores it in SQLite database."""
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()

    df = df.read_csv("data/sensor_data.csv")

    for _, row in df.iterrows():
        cursor.execute("INSERT INTO sensors (timestamp, temperature, vibration, pressure) VALUES (?,?,?,?)",
                       (row["timestamp"], row["temperature"], row["vibration"], 
                        row["pressure"]))
    conn.commit()
    conn.close()
    print("Sensor data stored in database successfully!")

if __name__ == "__main__":
    store_sensor_data()
