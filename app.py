import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
server = app.server

app.layout = dbc.Container([
        html.Div("Henry Pickersgill", style={'color':'white', 'text-align': 'center', 'background-color':'#172d4f', 'font-family': 'Open-Sans'}),
        html.Div("test", style={'color':'white', 'text-align': 'center', 'background-color':'#172d4f', 'font-family': 'Open-Sans'}),
        html.Div("Website contents here", style={'color': 'white', 'text-align': 'center', 'font-family': 'Open-Sans'})
    ])

server.run(debug=True)