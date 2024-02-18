import dash
from dash import Output, Input, State
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
                html.A("Home", id="home_link", className="navbar_link"),
                html.A("Programming", id="programming_link", className="navbar_link"),
                html.A("Piano", id="piano_link", className="navbar_link"),
                html.A("Photography", id="photography_link", className="navbar_link")
            ],
                className="heading_div"
        )
    ]),
    html.Div(style={"height": "5px", "background-color": "#172d4f"}),
    html.Div("home contents here", id="home_main_body", style={'display': 'block'}),
    html.Div("Programming contents here", id="programming_main_body", style={'display': 'none'}),
    html.Div("Piano contents here", id="piano_main_body", style={'display': 'none'}),
    html.Div("Photography contents here", id="photography_main_body", style={'display': 'none'})
])

### CALLBACKS ###
@app.callback(
    Output("home_main_body", "style"),
    Output("programming_main_body", "style"),
    Output("piano_main_body", "style"),
    Output("photography_main_body", "style"),
    Input("home_link", "n_clicks"),
    Input("programming_link", "n_clicks"),
    Input("piano_link", "n_clicks"),
    Input("photography_link", "n_clicks")
)
def show_hide_tabs(n_home, n_prog, n_piano, n_photo):
    trigger = dash.callback_context.triggered[0]['prop_id']
    if 'home' in trigger:
        return {"display": "block"}, {"display": "none"}, {"display": "none"}, {"display": "none"}
    elif 'prog' in trigger:
        return {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}
    elif 'piano' in trigger:
        return {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}
    elif 'photo' in trigger:
        return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "block"}
    return dash.no_update

app.run_server(host='0.0.0.0', port=8050, debug=True)