import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model_path, X_test, y_test):
    """Loads a trained model and evaluates its performance."""
    model = joblib.load(model_path)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    print(f"Model: {model_path}")
    print(f"Accuracy: {accuracy:.2f}")
    print(report)

if __name__ == "__main__":
    df = pd.read_csv("data/sensor_data.csv")
    X = df[['temperature', 'vibration', 'pressure']]
    y = df['fault']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    evaluate_model("models/fault_detection_rf.pkl", X_test, y_test)
    evaluate_model("models/fault_detection_xgb.pkl", X_test, y_test)
    