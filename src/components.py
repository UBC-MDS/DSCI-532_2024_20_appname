from dash import html, dcc
import dash_vega_components as dvc
from datetime import date

from src.data import country_codes

# Define components
title_header = [
    html.H1(
        children="Hotspot",
    ),
    html.H5(
        "How many kilotons of CO2 are emitted by countries across the world?"
    ),
]

page_footer = [
    html.P(f"Last Updated: {date.today()}"),
    html.P(
        [
            """Our Hotspot dashboard offers an easy and intuitive way to look at CO2
               emissions by different countries in the world, that allows for easy
               filtering by year range and country.
            """
        ]
    ),
    html.P(
        [
            "Made by: ",
            html.A("@farrandi", href="https://github.com/farrandi"),
            ", ",
            html.A("@monazhu", href="https://github.com/monazhu"),
            ", ",
            html.A("@juliaeveritt", href="https://github.com/juliaeveritt"),
            ", ",
            html.A("@Rachel0619", href="https://github.com/Rachel0619"),
        ]
    ),
    html.P(
        [
            "Repo: ",
            html.A(
                "Hotspot",
                href="https://github.com/UBC-MDS/DSCI-532_2024_20_hotspot",
            ),
        ]
    ),
]

# Inputs
year_slider = dcc.RangeSlider(
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
)

country_dropdown = dcc.Dropdown(
    id="country-dropdown",
    options=[{"label": name, "value": code} for name, code in country_codes.items()],
    multi=True,
)

# Outputs
world_map = dcc.Graph(figure={}, id="world-map")

total_co2 = html.H2(id="total-co2")

fun_fact = html.P(id="fun-fact")

top_emitters = dvc.Vega(
    id="top-emmitters",
    opt={"renderer": "svg", "actions": False},
    style={"width": "100%"},
)

global_temp_co2 = dvc.Vega(
    id="global-temp-co2",
    opt={"renderer": "svg", "actions": False},
    style={"width": "90%", "height": "250px"},
)
