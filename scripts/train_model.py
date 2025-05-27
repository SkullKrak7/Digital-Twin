import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import joblib
import os

# Get the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_sensor_data():
    """Fetches sensor data from SQLite and returns a DataFrame."""
    db_path = os.path.join(BASE_DIR, "sensor_data.db")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM sensors", conn)
    conn.close()
    return df

def preprocess_data(df):
    """Cleans and prepares data for model training."""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.drop(columns=['id'], inplace=True)

    # FIXED: added missing OR symbol between conditions
    df['fault'] = ((df['temperature'] > 80) | (df['vibration'] > 4.0) | (df['pressure'] > 90))
    df['fault'] = df['fault'].astype(int)

    return df

def train_ai_model(df):
    """Trains RandomForest and XGBoost models to detect faults."""
    X = df[['temperature', 'vibration', 'pressure']]
    y = df['fault']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xgb_model.fit(X_train, y_train)

    # Save models
    model_dir = os.path.join(BASE_DIR, "models")
    os.makedirs(model_dir, exist_ok=True)

    joblib.dump(rf_model, os.path.join(model_dir, "fault_detection_rf.pkl"))
    joblib.dump(xgb_model, os.path.join(model_dir, "fault_detection_xgb.pkl"))

    print("AI models trained and saved successfully!")

if __name__ == "__main__":
    df = load_sensor_data()
    df = preprocess_data(df)
    train_ai_model(df)
