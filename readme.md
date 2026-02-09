# Digital Twin: Industrial Monitoring Dashboard

**Simulated IoT Sensors | AI Fault Detection | Interactive Dashboard | Cloud Deployment**

## Overview

This project implements a Digital Twin monitoring system that simulates industrial machinery using synthetic IoT sensor data. It monitors parameters such as temperature, vibration, and pressure to detect faults using trained AI models. The system includes:

* Simulated sensor data generation
* Local SQLite database for storage
* Fault detection using Random Forest and XGBoost
* Interactive dashboard using Dash and Plotly (updates on page refresh)
* REST API using Flask
* Docker containerization
* Cloud-ready architecture (Heroku compatible)

**Note:** Dashboard updates on page refresh, not live streaming.

## Project Structure

```
digital_twin_project/
├── app/               
│   ├── __init__.py
│   ├── api.py
│   └── dashboard.py
│
├── data/              
│   └── sensor_data.csv
│
├── models/            
│   └── fault_detection_rf.pkl
│
├── scripts/           
│   ├── __init__.py
│   ├── data_gen.py
│   ├── init_db.py
│   ├── store_data.py
│   ├── fetch_data.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── main.py            
├── requirements.txt   
├── Dockerfile         
├── .gitignore         
└── README.md
```

## Key Technologies

* Python 3.13 (Docker: `python:3.13-slim-bookworm`)
* Flask and Dash (API and dashboard)
* pandas and numpy (data processing)
* sqlite3 (database)
* scikit-learn and xgboost (model training)
* plotly (visualization)
* joblib (model persistence)

## How It Works

### 1. Simulate Sensor Data

`data_gen.py` generates synthetic temperature, vibration, and pressure readings into a CSV.

### 2. Store Data in SQLite

* `init_db.py` initializes the database schema.
* `store_data.py` inserts CSV data into `sensor_data.db`.

### 3. Train AI Models

`train_model.py` trains RandomForest and XGBoost models based on fault rules, and saves them in the `models/` directory.

### 4. API Endpoint

`api.py` serves the 10 latest entries from the database at `/data`.

### 5. Real-Time Dashboard

`dashboard.py` polls the API every 2 seconds and renders a live chart and table.

### 6. CLI Launcher

`main.py` provides a menu with 6 options to run each component in sequence or together.

## Local Setup

### 1. Create and Activate Environment

```bash
conda create --name digital-twin-env python=3.13
conda activate digital-twin-env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Use the CLI

```bash
python main.py
```

Select from options 1–6 to:

* Generate data
* Initialize DB
* Train models
* Launch dashboard and API together

## Docker Deployment

### 1. Build the Image

```bash
docker build -t digital-twin .
```

### 2. Run the Container

```bash
docker run -it --rm -p 5000:5000 -p 8050:8050 digital-twin
```

### 3. Access Services

* API: [http://localhost:5000/data](http://localhost:5000/data)
* Dashboard: [http://localhost:8050](http://localhost:8050)

## (Optional) Heroku Deployment

### 1. Prepare Files

Ensure `requirements.txt` and `Procfile` exist:

**Procfile:**

```
web: gunicorn app.api:app
```

### 2. Deploy

```bash
heroku login
heroku create digital-twin-monitoring
heroku git:remote -a digital-twin-monitoring
git push heroku main
```

### 3. Access API

[https://digital-twin-monitoring.herokuapp.com/data](https://digital-twin-monitoring.herokuapp.com/data)

## Sample API Output

```json
[
  {
    "timestamp": "2025-03-18 12:00:02",
    "temperature": 78.2,
    "vibration": 3.2,
    "pressure": 60.5
  }
]
```

## Fault Prediction Logic

```python
fault = (
    temperature > 80
    or vibration > 4.0
    or pressure > 90
)
```

## Future Improvements

* Replace CSV step with real-time stream → DB
* Add Docker health checks and logs
* Use PostgreSQL for concurrency support
* Deploy full dashboard with domain and HTTPS

## Author

Built by Sai Karthik Kagolanu as a practical industrial simulation and monitoring project.

## License

Licensed under the MIT License. See LICENSE file for details.
