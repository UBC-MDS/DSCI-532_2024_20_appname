from dash import Dash, html
import dash_bootstrap_components as dbc

from src.callbacks import cache
import src.callbacks
from src.components import (
    title_header,
    page_footer,
    year_slider,
    country_dropdown,
    world_map,
    total_per_capita_button,
    co2_emissions_ranking,
    global_temp_co2,
    total_co2,
    fun_fact,
    year_header,
    figure_caption,
)

# Initialize Dash app
app = Dash(__name__, title="Hotspot", external_stylesheets=[dbc.themes.FLATLY])
server = app.server


# Initialize cache
cache.init_app(
    server, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "cache-directory"}
)

# Define layout
app.layout = dbc.Container(
    [
        # HEADER
        html.Div(
            title_header,
            className="app-header",
        ),
        html.Hr(),
        dbc.Row(
            [
                # First container, contains widgets (year range, countries) & key KPI
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                html.H3("Filter Options"),
                                html.Br(),
                                html.H5("Select Year Range"),
                                year_slider,
                                html.H5("Select Countries"),
                                country_dropdown,
                            ]
                        ),
                        dbc.Container(
                            [
                                html.H4("Total CO2 Emission:"),
                                total_co2,
                                year_header,
                                fun_fact,
                            ],
                            className="info-container",
                        ),
                        html.Footer(
                            page_footer,
                            className="app-footer",
                        ),
                    ],
                    className="app-widget",
                ),
                # Second container, contains map (left), top CO2 emitters (top right), &
                # temperature vs CO2 over time (bottom right)
                dbc.Col(
                    [
                        html.H4("World Map of CO2 Emissions"),
                        html.P(
                            """Hover over the graph and use box/lasso
                            select to select the countries on the map.
                            """,
                            style={"text-align": "center"},
                        ),
                        world_map,
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H4(
                                            "CO2 Emissions Ranking"
                                        ),
                                        co2_emissions_ranking,
                                        total_per_capita_button,
                                    ],
                                ),
                                dbc.Col(
                                    [
                                        html.H4(
                                            "Temperature and CO2 Emissions over Time"
                                        ),
                                        global_temp_co2,
                                        figure_caption,
                                    ]
                                ),
                            ],
                            className="bottom-container",
                        ),
                    ],
                    align="center",
                    md=9,
                    # className="app-output-col",
                ),
            ],
            className="app-row",
        ),
    ],
    className="app-container",
)


if __name__ == "__main__":
    app.run(debug=True)  # Remember to change to False before deploying
