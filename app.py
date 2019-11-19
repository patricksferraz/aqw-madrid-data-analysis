# %%

# -*- coding: utf-8 -*-
import dash
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

# %%
ma_token = (
    "pk."
    "eyJ1IjoicGF0cmlja3NmZXJyYXoiLCJhIjoiY2szNThueThrMDU0ZjNucjE2aWNhNmE3cCJ9"
    ".PAJSqXLEOUFCRCS8P8duiA"
)
ma_style = "mapbox://styles/patricksferraz/ck358pwmg06pu1ely6lguwwi3"

ARGS = {
    "wt-madrid": "dataset/extract/wt_madrid.h5",
    "aq-madrid": "dataset/extract/aq_madrid.h5",
}

# %%

df_wt = pd.HDFStore(ARGS.get("wt-madrid"))
df_aq = pd.HDFStore(ARGS.get("aq-madrid"))


# %%

LOWER_LIMIT_DATE = "2001"
weather = df_wt.get("master")
weather = weather.set_index("CET")
weather = weather.sort_values("CET")
weather.index = pd.to_datetime(weather.index)
weather = weather[weather.index >= LOWER_LIMIT_DATE]
df_wt.close()

# %%

stations = df_aq.get("master")
df_aq.close()

# %%

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

c_lat = float(stations[stations["name"] == "Parque del Retiro"]["lat"])
c_lon = float(stations[stations["name"] == "Parque del Retiro"]["lon"])
map = dcc.Graph(
    id="stations-map",
    figure={
        "data": [
            {
                "lat": stations["lat"],
                "lon": stations["lon"],
                "type": "scattermapbox",
                "text": stations["name"],
            }
        ],
        "layout": go.Layout(
            title="Teste",
            autosize=True,
            hovermode="closest",
            showlegend=False,
            mapbox={
                "accesstoken": ma_token,
                "style": ma_style,
                "center": {"lat": c_lat, "lon": c_lon},
                "pitch": 30,
                "zoom": 9.7,
            },
        ),
    },
)

app.layout = html.Div([map])

if __name__ == "__main__":
    app.run_server(debug=True)
