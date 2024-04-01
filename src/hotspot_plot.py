import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px


def plot_global_temp_co2(df, start_year=1850, end_year=2022):
    """
    Plots the global temperature and CO2 concentration from start_year to end_year.
    """
    co2_color = "red"
    temp_color = "blue"

    df_year = (
        df.query(f"{start_year} <= year <= {end_year}")
        .groupby("year")
        .aggregate({"co2": "sum", "temperature_change_from_co2": "mean"})
        .reset_index()
        .dropna()
    )

    base = alt.Chart(df_year).encode(
        alt.X("year:O", title="Year").axis(
            labelAngle=0, values=list(np.linspace(start_year, end_year, 20).astype(int))
        )
    )

    co2_line = base.mark_line(color=co2_color).encode(
        y=alt.Y("co2").title("CO2 Emissions"),
        tooltip=[alt.Tooltip("year:O"), alt.Tooltip("co2", title="CO2 Emissions")],
    )
    temp_line = base.mark_line(stroke=temp_color).encode(
        y=alt.Y("temperature_change_from_co2").title("Temperature Change"),
        tooltip=[
            alt.Tooltip("year:O"),
            alt.Tooltip("temperature_change_from_co2", title="Temperature Change"),
        ],
    )

    return (
        alt.layer(co2_line, temp_line)
        .resolve_scale(y="independent")
        .properties(
            title="Global CO2 emissions and temperature change over time",
            width=1000,
            height=400,
        )
        .configure_axisLeft(titleColor=co2_color, titleFontSize=12)
        .configure_axisRight(titleColor=temp_color, titleFontSize=12)
        .configure_title(fontSize=20)
    ).to_dict()


def plot_world_map(df, country_codes, start_year=1850, end_year=2022):
    """
    Plots the world map of CO2 emissions for the selected countries from start_year to end_year.
    """

    df_filtered = df.query(f"{start_year} <= year <= {end_year}")
    if country_codes:
        df_filtered = df_filtered[df_filtered.iso_code.isin(country_codes)]

    fig = px.choropleth(
        df_filtered,
        locations="iso_code",
        color="co2",
        color_continuous_scale="reds",
        labels={"co2": "CO2 Emissions"},
        hover_name="country",
        scope="world",
    )
    fig.update_layout(
        title_text="CO2 emissions by country",
        title_font_size=30,
        margin={"r": 0, "t": 55, "l": 0, "b": 0},
    )
    fig.update_geos(
        resolution=110,
        showcountries=True,
        showland=True,
        landcolor="lightgrey",
        countrycolor="darkgrey",
    )

    return fig
