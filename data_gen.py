import pandas as pd
import numpy as np
import time

def generate_sensor_data():
    """Simulates sensor readings for temperature, vibration and pressure"""
    data = {
        "timestamp": pd.Timestamp.now(),
        "temperature": np.random.uniform(30, 100),
        "vibration": np.random.uniform(0.1, 5.0),
        "pressure": np.random.uniform(10, 100)
    }
    return data
if __name__ =="__main__":
    for _ in range(10):
        print(generate_sensor_data())
        time.sleep(1)