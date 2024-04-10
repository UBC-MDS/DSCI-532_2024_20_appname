import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px

CO2_DENSITY = 1.98  # kg/m^3, src=wikipedia
ESB_VOLUME = 1047723.3  # m^3, src=https://www.esbnyc.com/sites/default/files/esb_fact_sheet_4_9_14_4.pdf
MAX_CO2 = 420e3  # GT

alt.data_transformers.enable("vegafusion")


def filter_data(df, country_codes, start_year=1900, end_year=2022):
    """
    Filters the data based on the selected countries and year range.
    """
    if country_codes:
        df = df[df.iso_code.isin(country_codes)]
    return df.query(f"{start_year} <= year <= {end_year}")


def plot_global_temp_co2(df, start_year=1900, end_year=2022):
    """
    Plots the global temperature and CO2 concentration from start_year to end_year.
    """
    co2_color = "#424254"
    temp_color = "#cc2a40"

    df_year = (
        df.groupby("year")
        .aggregate({"co2": "sum", "temperature_change_from_co2": "mean"})
        .reset_index()
        .dropna()
    )

    base = alt.Chart(df_year).encode(
        alt.X("year:O", title="Year").axis(
            labelAngle=-45,
            values=list(np.linspace(start_year, end_year, 20).astype(int)),
        )
    )

    co2_line = base.mark_line(color=co2_color).encode(
        y=alt.Y("co2").title("CO2 Emission (GT)"),
        tooltip=[alt.Tooltip("year:O"), alt.Tooltip("co2", title="CO2 Emissions (GT)")],
    )
    temp_line = base.mark_line(stroke=temp_color).encode(
        y=alt.Y("temperature_change_from_co2").title("Temperature Change (°C)"),
        tooltip=[
            alt.Tooltip("year:O"),
            alt.Tooltip("temperature_change_from_co2", title="Temperature Change"),
        ],
    )

    return (
        alt.layer(co2_line, temp_line)
        .resolve_scale(y="independent")
        .properties(
            width="container",
            height="container",
        )
        .configure_axisLeft(titleColor=co2_color, titleFontSize=12)
        .configure_axisRight(titleColor=temp_color, titleFontSize=12)
        .configure_title(fontSize=20)
    ).to_dict(format="vega")


def plot_world_map(df_filtered):
    """
    Plots the world map of CO2 emissions for the selected countries from start_year to end_year.
    """
    df_filtered = df_filtered.groupby(["iso_code", "country"]).sum().reset_index()

    fig = px.choropleth(
        df_filtered,
        locations="iso_code",
        color=np.log10(df_filtered["co2"] + 1),
        color_continuous_scale="Reds",
        range_color=(0, np.log10(MAX_CO2)),
        labels={"co2": "CO2 Emissions (GT)"},
        hover_name="country",
        scope="world",
    )
    fig.update_layout(
        margin={"r": 0, "t": 25, "l": 0, "b": 0},
        coloraxis_showscale=False,
        clickmode="event+select",
    )
    fig.update_geos(
        showcountries=True,
        showland=True,
        landcolor="lightgrey",
        countrycolor="darkgrey",
    )

    return fig


def plot_top_emitters(df_filtered, n=10):
    """
    Plots the top n CO2 emitters from start_year to end_year.
    """
    df_sorted = (
        df_filtered.groupby("country")
        .sum()
        .sort_values("co2", ascending=False)
        .head(n)
        .reset_index()
    )
    return (
        alt.Chart(df_sorted, width="container")
        .mark_bar()
        .encode(
            y=alt.Y("country", title="").sort("-x"),
            x=alt.X("co2", title="CO2 Emissions (GT)"),
        )
        .configure_mark(color="#cc2a40")
        .to_dict(format="vega")
    )


def get_total_co2_emissions(df_filtered):
    """
    Get the total CO2 emissions for the selected countries from start_year to end_year.
    """
    total_co2 = df_filtered[["co2"]].sum()  # Gt
    return total_co2.values[0]


def get_number_of_esb(total_co2_mass):
    """
    Get the number of Empire State Buildings that can be filled with the total CO2 emissions.
    """
    total_co2_mass_kg = total_co2_mass * 1e6  # Gt to kg
    total_co2_volume = total_co2_mass_kg / CO2_DENSITY  # kg to m^3
    return int(total_co2_volume / ESB_VOLUME)
