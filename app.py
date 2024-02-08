import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
server = app.server

def update_layout():
    body = dbc.Container([
        dash.html.Div("Hello")
    ])
    return body

app.layout = update_layout()