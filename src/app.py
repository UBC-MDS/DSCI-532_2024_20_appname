from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import src.hotspot_plot as hp
import dash_vega_components as dvc
import json

# Load data
df = pd.read_csv("data/processed/co2-data.csv")
with open("data/processed/country_codes.json", encoding="utf-8") as f:
    country_codes = json.load(f)

# Initialize Dash app
app = Dash(__name__, title="Hotspot", external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    [
        html.H1(children="Hotspot"),
        html.Hr(),
        dbc.Container(
            [
                html.H2("Filter Options"),
                html.H4("Select Year Range"),
                dcc.RangeSlider(
                    min=1900,
                    max=2022,
                    step=1,
                    value=[1900, 2022],
                    marks={
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
                html.H4("Select Countries"),
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
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Total CO2 emissions:"),
                        html.H2(id="total-co2", style={"color": "red"}),
                        html.Br(),
                        html.H4("Fun Fact!"),
                        html.P(id="fun-fact"),
                    ],
                    align="center",
                ),
                dbc.Col(
                    [
                        html.H2("World Map of CO2 Emissions"),
                        dcc.Graph(figure={}, id="world-map"),
                    ],
                    width=8,
                ),
            ],
            justify="center",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Temperature and CO2 Emissions over Time"),
                        dvc.Vega(
                            id="global-temp-co2",
                            opt={"renderer": "svg", "actions": False},
                            style={"width": "100%"},
                        ),
                    ],
                    width=7,
                ),
                dbc.Col(
                    [
                        html.H3("Top CO2 Emitters"),
                        dvc.Vega(
                            id="top-emmitters",
                            opt={"renderer": "svg", "actions": False},
                            style={"width": "100%"},
                        ),
                    ]
                ),
            ],
            justify="center",
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
    Input("country-dropdown", "value"),
)
def update_global_temp_co2(year, country):
    """
    Update the global temperature and CO2 plot based on the year range selected.
    """
    return hp.plot_global_temp_co2(df, country, start_year=year[0], end_year=year[1])


@callback(
    Output("top-emmitters", "spec"),
    Input("year-slider", "value"),
    Input("country-dropdown", "value"),
)
def update_top_emitters(year, country):
    """
    Update the top CO2 emitters plot based on the year range selected.
    """
    return hp.plot_top_emitters(df, country, start_year=year[0], end_year=year[1])


@callback(
    Output("total-co2", "children"),
    Input("year-slider", "value"),
    Input("country-dropdown", "value"),
)
def update_total_co2(year, country):
    """
    Update the total CO2 emissions based on the year range selected.
    """
    total_co2 = hp.get_total_co2_emissions(
        df, country, start_year=year[0], end_year=year[1]
    )
    return f"{total_co2*1000:,.0f} kT"


@callback(
    Output("fun-fact", "children"),
    Input("year-slider", "value"),
    Input("country-dropdown", "value"),
)
def update_fun_fact(year, country):
    """
    Update the fun fact based on the total CO2 emissions.
    Funfact: How many empire state buildings is equivalent to the total CO2 emissions.
    """
    total_co2 = hp.get_total_co2_emissions(
        df, country, start_year=year[0], end_year=year[1]
    )
    num_empire_state_buildings = hp.get_number_of_esb(total_co2)
    return f"Equivalent to {num_empire_state_buildings:,} Empire State Buildings!"


if __name__ == "__main__":
    app.run(debug=False)  # Remember to change to False before deploying
