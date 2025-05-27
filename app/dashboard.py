import dash
from dash import dcc, html, dash_table
import pandas as pd
import requests
import plotly.express as px
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
server = app.server

def fetch_data():
    """Fetches sensor data from the API."""
    response = requests.get("http://127.0.0.1:5000/data")
    return pd.DataFrame(response.json()) if response.status_code == 200 else pd.DataFrame()

app.layout = html.Div([
    html.H1("Digital Twin - Industrial Monitoring", style={"textAlign": "center"}),
    dash_table.DataTable(
        id="sensor-table",
        columns=[{"name": i, "id": i} for i in ["timestamp", "temperature", "vibration", "pressure"]],
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "center"},
    ),
    dcc.Graph(id="sensor-graph"),
    dcc.Interval(id="interval-component", interval=2000, n_intervals=0)
])

@app.callback(
    [Output("sensor-table", "data"), Output("sensor-graph", "figure")],
    [Input("interval-component", "n_intervals")]
)
def update_dashboard(n):
    """Updates dashboard with the latest sensor data."""
    df = fetch_data()
    if df.empty:
        return [], {}
    fig = px.line(df, x="timestamp", y=["temperature", "vibration", "pressure"], title="Sensor Readings Over Time", markers=True)
    fig.update_layout(xaxis_title="Timestamp", yaxis_title="Sensor Values")
    return df.to_dict("records"), fig

if __name__ == "__main__":
    app.run(debug=True, port=8050)
