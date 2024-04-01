from dash import Dash, html, dash_table, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import hotspot_plot as hp
import dash_vega_components as dvc

# Load data
df = pd.read_csv("data/raw/owid-co2-data.csv")

# Initialize Dash app
app = Dash(__name__, title="Hotspot", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H1(children="Hotspot"),
        html.Hr(),
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
        dvc.Vega(id="global-temp-co2", opt={"renderer": "svg", "actions": False}),
    ]
    # [
    #     html.Header("Simple Dash App: Hotspot", className="display-4"),
    #     dash_table.DataTable(data=df.head(10).to_dict("records"), page_size=10),
    #     dcc.Graph(
    #         figure=px.scatter(
    #             df.head(10), x="gdp", y="population", color="country", size="year"
    #         )
    #     ),
    # ]
)


# Controls for Interactive Plot
@callback(
    Output("global-temp-co2", "spec"),
    Input("year-slider", "value"),
)
def update_global_temp_co2(value):
    return hp.plot_global_temp_co2(df, start_year=value[0], end_year=value[1])


if __name__ == "__main__":
    app.run(debug=True)
