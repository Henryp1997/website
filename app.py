import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        html.Div("Henry Pickersgill", className="heading_div"),
        html.Div("htap2@live.co.uk | 07470521144", className="heading_div"),
    ]),
    html.Div(style={"height": "5px", "background-color": "#172d4f"}),
    dbc.Row([
        html.Div([
                html.A("Home", className="navbar_link"),
                html.A("Programming", className="navbar_link"),
                html.A("Placeholder1", className="navbar_link"),
                html.A("Placeholder2", className="navbar_link")
            ],
                className="heading_div"
        )
    ]),
    html.Div(style={"height": "5px", "background-color": "#172d4f"}),
])

server.run(debug=True)