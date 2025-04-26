import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import joblib

def load_sensor_data():
    """Fetches sensor data from SQLite and returns a DataFrame."""
    conn = sqlite3.connect("sensor_data.db")
    df = pd.read_sql("sensor_data.db")
    conn.close()
    return df

def preprocess_data(df):
    """Cleans and prepares data for model training"""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.drop(columns=['id'], inplace=True)

    df['fault'] = (df['temperature']>80) | (df['vibration'] > 4.0) (df['pressure'] > 90)
    df['fault'] = df['fault'].astype(int)

    return df

def train_ai_model(df):
    X = df[['temperature', 'vibration', 'pressure']]
    y = df['fault']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_model = RandomForestClassifier(n_estiamtors=100, random_state=42)
    rf_model.fit(X_train, y_train)

    xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xgb_model.fit(X_train, y_train)

    joblib.dump(rf_model, "models/fault_detection_rf.pkl")
    joblib.dump(xgb_model, "models/fault_detection_xgb.pkl")

    print("AI models trained and saved successfully!")

    if __name__ == "__main__":
        df = load_sensor_data()
        df = preprocess_data(df)
        train_ai_model(df)

