import dash
from dash import dcc, html, dash_table
import pandas as pd
import requests
import plotly.express as px

app = dash.Dash(__name__)

def fetch_data():
    """Fetches sensor data from the API."""
    response = requests.get("http://127.0.0.1:5000/data")
    return pd.DataFrame(response.json()) if response.status_code == 200 else pd.DataFrame()

app.layout = html.Div([
    html.H1("Digital Twin - Industrial Monitoring", style={"textAlign": "center"}),
    dash_table.DataTable(
        id="sensor-table",
        columns=[{"name": i, "id": i} for i in ["timestamp","temperature", "vibration","pressure"]],
        style_table={"overflowX":"auto"}
    ),

    dcc.Graph(id="sensor-graph"),

    dcc.Interval(id="interval-component", interval=2000, n_intervals=0)
])

@app.callback(
    [dash.dependencies.Output("sensor-table", "data"),
     dash.dependencies.Output("sensor-graph", "figure")],
     [dash.dependencies.Input("interval-component", interval=2000, n_intervals=0)]
)

def update_dashborad(n):
    """Updates dashboard with the latest ensor data."""
    df = fetch_data()

    fig = px.line(df, x="timestamp", y=["temperature", "vibration","pressure"],
                                        title="Sensor Readings over Time")
    return df.to_dict("records"), fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)