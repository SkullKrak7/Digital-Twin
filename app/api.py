import sqlite3
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

def fetch_latest_data():
    """Fetches the last 10 sensor readings from the database."""
    conn = sqlite3.connect("sensor_data.db")
    df = pd.read_sql("SELECT * FROM sensors ORDER BY id DESC LIMIT 10", conn)
    conn.close()
    return df.to_dict(orient="records")

@app.route("/data", methods=["GET"])
def get_sensor_data():
    """API endpoint return the latest sensor readings."""
    data = fetch_latest_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)