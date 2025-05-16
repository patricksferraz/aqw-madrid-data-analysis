# %%

# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
import dash
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Mapbox token from environment variable
ma_token = os.getenv('MAPBOX_TOKEN')
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

UPPER_LIMIT_DATE = "2016"
stations = df_aq.get("master")
emissions = {}

for st in stations["id"]:
    aux = df_aq[str(st)]
    aux = aux.sort_values("date")
    aux.index = pd.to_datetime(aux.index)
    emissions[st] = aux[aux.index < UPPER_LIMIT_DATE]

df_aq.close()

# %%

navbar = html.Center(
    [html.H1("Air Quality and Weather in Madrid - 2001 to 2016")]
)

# %%

c_lat = float(stations[stations["name"] == "Parque del Retiro"]["lat"])
c_lon = float(stations[stations["name"] == "Parque del Retiro"]["lon"])
stations_map = dcc.Graph(
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
            autosize=True,
            hovermode="closest",
            showlegend=False,
            height=700,
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

# %%

body = html.Div(
    dbc.Row(
        [dbc.Col(stations_map, md=7), dbc.Col(html.Div(), md=5)],
        no_gutters=True,
    )
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True)
