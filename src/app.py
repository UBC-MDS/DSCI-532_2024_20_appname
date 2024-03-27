from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/raw/owid-co2-data.csv')
df = df[['country', 'year', 'population', 'gdp']]
df = df.dropna()

# Initialize Dash app
app = Dash(__name__, title='Hotspot', external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Header('Simple Dash App: Hotspot', className='display-4'),
    dash_table.DataTable(data=df.head(10).to_dict('records'), page_size=10),
    dcc.Graph(figure=px.scatter(df.head(10), x='gdp', y='population', color='country', size='year'))
])

if __name__ == '__main__':
    app.run(debug=True)