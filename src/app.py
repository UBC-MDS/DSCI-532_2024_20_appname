from dash import Dash, html
import dash_bootstrap_components as dbc

import src.callbacks
from src.components import (
    title_header,
    page_footer,
    year_slider,
    country_dropdown,
    world_map,
    top_emitters,
    global_temp_co2,
    information_text,
)

# Initialize Dash app
app = Dash(__name__, title="Hotspot", external_stylesheets=[dbc.themes.FLATLY])
server = app.server


# Define layout
app.layout = dbc.Container(
    [
        # HEADER
        html.Div(
            title_header,
            className="app-header",
        ),
        # First container, contains widgets (year range, countries) & key KPI
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Filter Options"),
                        html.H4("Select Year Range"),
                        year_slider,
                        html.H4("Select Countries"),
                        country_dropdown,
                    ],
                ),
                dbc.Col(
                    information_text,
                    align="center",
                    md=5,
                ),
            ],
            className="app-row",
        ),
        html.Br(),
        # Second container, contains map (left), top CO2 emitters (top right), &
        # temperature vs CO2 over time (bottom right)
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("World Map of CO2 Emissions"),
                        world_map,
                    ],
                    md=7,
                ),
                dbc.Col(
                    [
                        html.H4("Top CO2 Emitters"),
                        top_emitters,
                        html.H4("Temperature and CO2 Emissions over Time"),
                        global_temp_co2,
                    ],
                    align="center",
                ),
            ],
            className="app-row",
        ),
        html.Footer(
            page_footer,
            className="app-footer",
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)  # Remember to change to False before deploying
