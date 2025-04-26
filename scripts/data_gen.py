import pandas as pd
import numpy as np
import time
import os


def generate_sensor_data():
    """Simulates sensor readings for temperature, vibration, and pressure.
    Generates IoT sensor readings and stores them in a CSV file."""

    # Define safe path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)  # create data/ if not exists
    file_path = os.path.join(data_dir, "sensor_data.csv")

    data_list = []
    for _ in range(100):
        data = {
            "timestamp": pd.Timestamp.now(),
            "temperature": np.random.uniform(30, 100),
            "vibration": np.random.uniform(0.1, 5.0),
            "pressure": np.random.uniform(10, 100)
        }
        data_list.append(data)
        time.sleep(0.5)  # simulate real-time data arrival

    df = pd.DataFrame(data_list)
    df.to_csv(file_path, index=False)
    print(f"Sensor data saved to {file_path}")


if __name__ == "__main__":
    generate_sensor_data()
