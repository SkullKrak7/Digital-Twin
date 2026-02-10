# Digital Twin: Industrial Monitoring System

**Real-time IoT Monitoring | Anomaly Detection | Interactive Dashboard | Docker Deployment**

## Overview

A production-ready Digital Twin system for industrial equipment monitoring with real-time sensor visualization, anomaly detection, and predictive analytics. Features a modern teal/cyan themed dashboard with live metric cards, threshold-based alerts, and automated data refresh.

**Key Capabilities:**
* Real-time sensor monitoring (temperature, vibration, pressure)
* Automated anomaly detection with threshold alerts
* Live metric cards showing current sensor values
* Interactive time-series visualization
* REST API for sensor data access
* Docker Compose orchestration
* Industry-standard teal/cyan color scheme

---

## Quick Start

### Docker Compose (Recommended)

```bash
docker-compose up -d
```

**Access:**
- Dashboard: **http://localhost:8050**
- API: **http://localhost:5000/data**

### Manual Setup

Requires **Python 3.13+**.

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize system
python scripts/data_gen.py
python scripts/init_db.py
python scripts/store_data.py

# Start services (in separate terminals)
python app/api.py        # Port 5000
python app/dashboard.py  # Port 8050
```

---

## Architecture

### Components

1. **Data Generation** (`scripts/data_gen.py`)
   - Generates synthetic sensor readings
   - Simulates industrial equipment behavior

2. **Database** (`scripts/init_db.py`, `scripts/store_data.py`)
   - SQLite storage for sensor history
   - Efficient time-series queries

3. **REST API** (`app/api.py`)
   - Flask endpoint at `/data`
   - Returns latest 10 sensor readings
   - JSON response format

4. **Dashboard** (`app/dashboard.py`)
   - Dash/Plotly interactive UI
   - Auto-refresh every 2 seconds
   - Real-time anomaly detection

### Docker Compose Flow

```yaml
init → api → dashboard
  ↓      ↓       ↓
 Data   REST   Live UI
```

The `init` service runs data generation and database setup, then `api` and `dashboard` start automatically.

---

## Dashboard Features

### Live Metric Cards
- **Temperature**: Current reading with °C unit
- **Vibration**: Frequency in Hz
- **Pressure**: Bar measurement
- **System Status**: ✅ Normal or ⚠️ Alert

### Anomaly Detection
Real-time threshold monitoring:
- Temperature > 85°C → High temperature alert
- Vibration > 0.8 Hz → High vibration alert
- Pressure > 95 bar → High pressure alert

### Visualization
- Multi-line time-series graph
- Dark theme with teal accents
- Responsive layout (no scrollbars)
- Recent readings table (5 entries)

---

## API Endpoints

### Get Sensor Data
```bash
GET /data

Response:
[
  {
    "id": 1,
    "timestamp": "2026-02-10 14:30:00",
    "temperature": 78.5,
    "vibration": 0.65,
    "pressure": 82.3
  },
  ...
]
```

---

## Project Structure

```text
.
├── app/
│   ├── api.py              # Flask REST API
│   ├── dashboard.py        # Dash dashboard with anomaly detection
│   └── __init__.py
├── scripts/
│   ├── data_gen.py         # Sensor data generator
│   ├── init_db.py          # Database initialization
│   ├── store_data.py       # CSV to DB loader
│   ├── fetch_data.py       # Data retrieval utility
│   ├── train_model.py      # ML model training
│   ├── evaluate_model.py   # Model evaluation
│   └── __init__.py
├── data/
│   └── sensor_data.csv     # Generated sensor readings
├── models/
│   └── fault_detection_rf.pkl  # Trained ML model
├── main.py                 # CLI launcher
├── docker-compose.yml      # Multi-container orchestration
├── Dockerfile              # Container definition
├── requirements.txt
└── README.md
```

---

## Technologies

**Backend:**
- Python 3.13
- Flask (REST API)
- Dash + Plotly (Dashboard)
- SQLite (Database)

**ML/Analytics:**
- pandas, numpy (Data processing)
- scikit-learn, xgboost (Fault detection models)
- joblib (Model persistence)

**Deployment:**
- Docker + Docker Compose
- Multi-stage container orchestration

---

## UI Design

**Color Scheme**: Teal/Cyan industrial monitoring theme
- Background: Dark slate (#020617)
- Primary: Teal (#14b8a6)
- Accents: Cyan borders (#2dd4bf)
- Purpose: Professional monitoring aesthetic

**Layout**: Full-width responsive design with 4-column metric grid

---

## Anomaly Detection Logic

```python
def detect_anomalies(df):
    latest = df.iloc[0]
    anomalies = []
    
    if latest['temperature'] > 85:
        anomalies.append("⚠️ High temperature")
    if latest['vibration'] > 0.8:
        anomalies.append("⚠️ High vibration")
    if latest['pressure'] > 95:
        anomalies.append("⚠️ High pressure")
    
    return anomalies if anomalies else ["✅ All systems normal"]
```

---

## Development

### Run Tests
```bash
python -m pytest tests/
```

### CLI Menu
```bash
python main.py
```

Options:
1. Generate sensor data
2. Initialize database
3. Store data in DB
4. Fetch latest data
5. Train fault detection model
6. Run API + Dashboard together

---

## Future Enhancements

- [ ] Predictive maintenance ML models
- [ ] Historical trend analysis
- [ ] Multi-equipment monitoring
- [ ] Alert notifications (email/SMS)
- [ ] PostgreSQL for production scale
- [ ] Kubernetes deployment
- [ ] Real-time streaming (Kafka/MQTT)

---

## Author

Built by Sai Karthik Kagolanu as a demonstration of industrial IoT monitoring and digital twin concepts.

---

## License

MIT License. See LICENSE file for details.
