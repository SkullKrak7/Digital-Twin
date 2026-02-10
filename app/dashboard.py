import dash
from dash import dcc, html, dash_table
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
server = app.server

def fetch_data():
    """Fetches sensor data from the API."""
    response = requests.get("http://api:5000/data")
    return pd.DataFrame(response.json()) if response.status_code == 200 else pd.DataFrame()

def detect_anomalies(df):
    """Simple anomaly detection based on thresholds."""
    if df.empty:
        return []
    latest = df.iloc[0]
    anomalies = []
    if latest['temperature'] > 85:
        anomalies.append(f"⚠️ High temperature: {latest['temperature']:.1f}°C")
    if latest['vibration'] > 0.8:
        anomalies.append(f"⚠️ High vibration: {latest['vibration']:.2f} Hz")
    if latest['pressure'] > 95:
        anomalies.append(f"⚠️ High pressure: {latest['pressure']:.1f} bar")
    return anomalies if anomalies else ["✅ All systems normal"]

app.layout = html.Div([
    html.Div([
        html.H1("🏭 Digital Twin - Industrial Monitoring System", 
                style={"textAlign": "center", "marginBottom": "10px", "color": "#14b8a6", "fontSize": "2.5rem", "fontWeight": "700"}),
        html.P("Real-time sensor data visualization and anomaly detection", 
               style={"textAlign": "center", "color": "#64748b", "marginBottom": "30px", "fontSize": "1.1rem"}),
    ]),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div("🌡️", style={"fontSize": "2rem"}),
                    html.Div("Temperature", style={"fontSize": "0.9rem", "color": "#94a3b8", "marginTop": "5px"}),
                    html.Div(id="temp-value", children="--°C", style={"fontSize": "1.8rem", "fontWeight": "700", "color": "#14b8a6", "marginTop": "8px"}),
                ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "25px", "borderRadius": "16px", "textAlign": "center", "border": "1px solid #2dd4bf"}),
                
                html.Div([
                    html.Div("📊", style={"fontSize": "2rem"}),
                    html.Div("Vibration", style={"fontSize": "0.9rem", "color": "#94a3b8", "marginTop": "5px"}),
                    html.Div(id="vib-value", children="-- Hz", style={"fontSize": "1.8rem", "fontWeight": "700", "color": "#14b8a6", "marginTop": "8px"}),
                ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "25px", "borderRadius": "16px", "textAlign": "center", "border": "1px solid #2dd4bf"}),
                
                html.Div([
                    html.Div("⚡", style={"fontSize": "2rem"}),
                    html.Div("Pressure", style={"fontSize": "0.9rem", "color": "#94a3b8", "marginTop": "5px"}),
                    html.Div(id="press-value", children="-- bar", style={"fontSize": "1.8rem", "fontWeight": "700", "color": "#14b8a6", "marginTop": "8px"}),
                ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "25px", "borderRadius": "16px", "textAlign": "center", "border": "1px solid #2dd4bf"}),
                
                html.Div([
                    html.Div("🔔", style={"fontSize": "2rem"}),
                    html.Div("System Status", style={"fontSize": "0.9rem", "color": "#94a3b8", "marginTop": "5px"}),
                    html.Div(id="status-value", children="Monitoring...", style={"fontSize": "1.1rem", "fontWeight": "600", "color": "#14b8a6", "marginTop": "8px"}),
                ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "25px", "borderRadius": "16px", "textAlign": "center", "border": "1px solid #2dd4bf"}),
            ], style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "20px", "marginBottom": "25px"}),
            
            html.Div([
                html.H3("📈 Sensor Trends Over Time", style={"color": "#14b8a6", "marginBottom": "20px", "fontSize": "1.4rem"}),
                dcc.Graph(id="sensor-graph", style={"height": "450px"}),
            ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "30px", "borderRadius": "16px", "border": "1px solid #334155"}),
        ]),
        
        html.Div([
            html.Div([
                html.H3("🚨 Anomaly Detection", style={"color": "#14b8a6", "marginBottom": "15px", "fontSize": "1.2rem"}),
                html.Div(id="anomaly-alerts", children=["Initializing..."], style={"fontSize": "0.95rem", "lineHeight": "1.8"}),
            ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "25px", "borderRadius": "16px", "border": "1px solid #334155"}),
        ], style={"marginTop": "25px"}),
        
        html.Div([
            html.H3("📋 Recent Sensor Readings", style={"color": "#14b8a6", "marginBottom": "20px", "fontSize": "1.4rem"}),
            dash_table.DataTable(
                id="sensor-table",
                columns=[{"name": i, "id": i} for i in ["timestamp", "temperature", "vibration", "pressure"]],
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "center", "padding": "14px", "backgroundColor": "#1e293b", "color": "#e2e8f0", "border": "1px solid #334155", "fontSize": "13px"},
                style_header={"backgroundColor": "#0f172a", "fontWeight": "700", "color": "#14b8a6", "fontSize": "14px", "border": "1px solid #2dd4bf"},
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#0f172a"}
                ],
                page_size=5,
            ),
        ], style={"background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", "padding": "30px", "borderRadius": "16px", "border": "1px solid #334155", "marginTop": "25px"}),
    ]),
    
    dcc.Interval(id="interval-component", interval=2000, n_intervals=0)
], style={"padding": "40px 60px", "backgroundColor": "#020617", "minHeight": "100vh", "maxWidth": "100%", "overflow": "hidden"})

@app.callback(
    [Output("sensor-table", "data"), Output("sensor-graph", "figure"), 
     Output("temp-value", "children"), Output("vib-value", "children"), Output("press-value", "children"),
     Output("status-value", "children"), Output("anomaly-alerts", "children")],
    [Input("interval-component", "n_intervals")]
)
def update_dashboard(n):
    """Updates dashboard with the latest sensor data."""
    df = fetch_data()
    if df.empty:
        return [], {}, "--°C", "-- Hz", "-- bar", "No Data", ["Waiting for data..."]
    
    latest = df.iloc[0]
    temp_val = f"{latest['temperature']:.1f}°C"
    vib_val = f"{latest['vibration']:.2f} Hz"
    press_val = f"{latest['pressure']:.1f} bar"
    
    anomalies = detect_anomalies(df)
    status = "⚠️ ALERT" if len(anomalies) > 0 and "⚠️" in anomalies[0] else "✅ Normal"
    
    fig = px.line(df, x="timestamp", y=["temperature", "vibration", "pressure"], 
                  title="", markers=True)
    fig.update_layout(
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        font={"color": "#e2e8f0"},
        xaxis={"gridcolor": "#334155", "title": ""},
        yaxis={"gridcolor": "#334155", "title": "Sensor Values"},
        legend={"bgcolor": "#1e293b", "bordercolor": "#334155", "borderwidth": 1},
        margin={"l": 50, "r": 20, "t": 20, "b": 50}
    )
    fig.update_traces(line={"width": 3})
    
    alert_divs = [html.Div(a, style={"marginBottom": "8px", "color": "#ef4444" if "⚠️" in a else "#22c55e"}) for a in anomalies]
    
    return df.to_dict("records"), fig, temp_val, vib_val, press_val, status, alert_divs

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8050)
