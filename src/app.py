from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import hotspot_plot as hp
import dash_vega_components as dvc
import json

# Load data
df = pd.read_csv("data/raw/owid-co2-data.csv")
with open("data/processed/country_codes.json", encoding="utf-8") as f:
    country_codes = json.load(f)

# Initialize Dash app
app = Dash(__name__, title="Hotspot", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H1(children="Hotspot"),
        html.Hr(),
        dbc.Container(
            [
                html.H2("Select Year Range"),
                dcc.RangeSlider(
                    min=1850,
                    max=2022,
                    step=1,
                    value=[1850, 2022],
                    marks={
                        1850: "1850",
                        1900: "1900",
                        1950: "1950",
                        2000: "2000",
                        2022: "2022",
                    },
                    tooltip={"placement": "bottom"},
                    pushable=20,
                    id="year-slider",
                    updatemode="drag",
                ),
                html.H2("Select Countries"),
                dcc.Dropdown(
                    id="country-dropdown",
                    options=[
                        # country_codes
                        {"label": name, "value": code}
                        for name, code in country_codes.items()
                    ],
                    multi=True,
                ),
            ]
        ),
        dcc.Graph(figure={}, id="world-map"),
        dvc.Vega(
            id="global-temp-co2",
            opt={"renderer": "svg", "actions": False},
        ),
    ]
)


# Controls for Interactive Plot
@callback(
    Output("world-map", "figure"),
    Input("year-slider", "value"),
    Input("country-dropdown", "value"),
)
def update_world_map(year, country):
    """
    Update the world map based on the year range and selected countries.
    """
    return hp.plot_world_map(df, country, start_year=year[0], end_year=year[1])


@callback(
    Output("global-temp-co2", "spec"),
    Input("year-slider", "value"),
)
def update_global_temp_co2(value):
    """
    Update the global temperature and CO2 plot based on the year range selected.
    """
    return hp.plot_global_temp_co2(df, start_year=value[0], end_year=value[1])


if __name__ == "__main__":
    app.run(debug=True)
