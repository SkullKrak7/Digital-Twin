import pandas as pd
import numpy as np
import time

def generate_sensor_data():
    """Simulates sensor readings for temperature, vibration and pressure
    Generates IoT sensor readings and stores them in a CSV file."""

    data_list=[]
    for _ in range(100):
        data = {
        "timestamp": pd.Timestamp.now(),
        "temperature": np.random.uniform(30, 100),
        "vibration": np.random.uniform(0.1, 5.0),
        "pressure": np.random.uniform(10, 100)
    }
        data_list.append(data)
        time.sleep(0.5)

    df = pd.DataFrame(data_list)

    df.to_csv("data/sensor_data.csv", index=False)
    print("Sensor data saved to data/sensor_data.csv")

if __name__ == "__main__":
    generate_sensor_data()
