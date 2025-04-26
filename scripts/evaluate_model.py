import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Get the project root path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def evaluate_model(model_path, X_test, y_test):
    """Loads a trained model, evaluates its performance, and plots confusion matrix."""
    model = joblib.load(model_path)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    print(f"\n🔹 Model: {os.path.basename(model_path)}")
    print(f"✅ Accuracy: {accuracy:.2f}")
    print(report)

    # Plot confusion matrix
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title(f'Confusion Matrix for {os.path.basename(model_path)}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

if __name__ == "__main__":
    # Load raw sensor data
    csv_path = os.path.join(BASE_DIR, "data", "sensor_data.csv")
    df = pd.read_csv(csv_path)

    # Generate fault labels
    df['fault'] = (df['temperature'] > 80) | (df['vibration'] > 4.0) | (df['pressure'] > 90)
    df['fault'] = df['fault'].astype(int)

    # Feature/Target split
    X = df[['temperature', 'vibration', 'pressure']]
    y = df['fault']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Evaluate both models
    model_rf_path = os.path.join(BASE_DIR, "models", "fault_detection_rf.pkl")
    model_xgb_path = os.path.join(BASE_DIR, "models", "fault_detection_xgb.pkl")
    evaluate_model(model_rf_path, X_test, y_test)
    evaluate_model(model_xgb_path, X_test, y_test)
