# Digital Twin: Real-Time Industrial Monitoring System

> Simulated IoT Sensors • AI Fault Detection • Live Dashboard • Cloud Deployment

---

## 🔧 Project Overview

This project implements a **Digital Twin** system that simulates industrial machinery using synthetic IoT sensor data. It monitors parameters like **temperature**, **vibration**, and **pressure** to detect faults in real-time using trained AI models. The system features:

- Simulated real-world sensor data generation
- Local SQLite database for data storage
- AI-based fault detection using **Random Forest** and **XGBoost**
- Interactive real-time dashboard with **Dash + Plotly**
- RESTful API with **Flask**
- Cloud deployment-ready (Heroku-compatible)

---

## 🧱 Project Structure

```
digital_twin_project/
├── app/               # Flask API and Dash dashboard
│   ├── api.py
│   └── dashboard.py
│
├── data/              # Simulated sensor CSVs
│   └── sensor_data.csv
│
├── models/            # Trained AI models
│   └── fault_detection_rf.pkl
│
├── scripts/           # Sensor generation, database, model training
│   ├── data_gen.py
│   ├── init_db.py
│   ├── store_data.py
│   ├── fetch_data.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

---

## 🔌 Key Technologies

- **Python 3.8+**
- **Flask** + **Dash** for web backend & dashboard
- **pandas**, **numpy** for data generation
- **sqlite3** for local data storage
- **scikit-learn**, **xgboost** for AI fault detection
- **plotly** for interactive graphing
- **joblib** for model serialization

---

## 🚀 How It Works

### 1. Simulate Sensor Data

`data_gen.py` generates fake industrial sensor readings and stores them in a CSV file.

### 2. Store Data in SQLite

`init_db.py` initializes the database, and `store_data.py` inserts generated readings into `sensor_data.db`.

### 3. Train AI Models

- Loads the sensor data from the database
- Labels records as faulty if:
  - Temperature > 80°C
  - Vibration > 4.0 m/s²
  - Pressure > 90 bar
- Trains two models: `RandomForestClassifier` and `XGBoost`
- Saves them to `models/`

### 4. API Backend (Flask)

- `/data`: Returns last 10 sensor readings

### 5. Real-Time Dashboard (Dash)

- Auto-refreshes every 2 seconds
- Displays live sensor values and trend graph

---

## 🖥️ Local Setup

### 1. Create & Activate Conda Environment

```bash
conda create --name digital-twin-env python=3.8
conda activate digital-twin-env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
# Generate sensor data
python scripts/data_gen.py

# Initialize database
python scripts/init_db.py

# Store sensor data
python scripts/store_data.py

# Train AI models
python scripts/train_model.py

# Evaluate models (optional)
python scripts/evaluate_model.py
```

### 4. Launch Backend API

```bash
python app/api.py
```

Visit: [http://localhost:5000/data](http://localhost:5000/data)

### 5. Launch Dashboard

```bash
python app/dashboard.py
```

Visit: [http://localhost:8050](http://localhost:8050)

---

## ☁️ Cloud Deployment (Heroku)

### 1. Prepare Files

- `requirements.txt`
- `Procfile`:

```
web: gunicorn app.api:app
```

### 2. Deploy

```bash
heroku login
heroku create digital-twin-monitoring
heroku git:remote -a digital-twin-monitoring
git push heroku master
```

### 3. Live API URL

Visit: `https://digital-twin-monitoring.herokuapp.com/data`

---

## 📊 Sample Output

```
{'timestamp': '2025-03-18 12:00:02', 'temperature': 78.2, 'vibration': 3.2, 'pressure': 60.5}
...
```

## 🧠 Fault Prediction Logic

```
fault = (
    temperature > 80
    OR vibration > 4.0
    OR pressure > 90
)
```

---

## 📎 Notes

- Sensor simulation uses `np.random.uniform()` to mimic real-world variance
- Dashboard is auto-refreshing (every 2s)
- AI models saved in `models/` using `joblib`

---

## 🧼 To Do / Improvements

- [ ] Replace CSV pipeline with direct DB inserts
- [ ] Add Docker support
- [ ] Switch from SQLite to PostgreSQL
- [ ] Deploy dashboard as well to Heroku

---

## 👨‍💻 Author

Built by [Sai Karthik Kagolanu] as part of a real-world industrial simulation project.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.