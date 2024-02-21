import dash
from dash import Output, Input, State
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
server = app.server

right_arrow = "\u25b8"
down_arrow = "\u25be"
hollow_bullet = "\u25e6"
solid_bullet = "\u2022"

st_block = {"display": "block"}
st_none = {"display": "none"}
nop = dash.no_update

home_style = {
    'font-size': '14px',
    'background-color': '#f0f0f0',
    'color': 'black',
    'font-family': 'Open-Sans',
    'width': '60%',
    'margin': 'auto',
    'border-radius': '0.5rem',
    'padding': '0.5rem'
}
prog_style = {}
piano_style = {}
photo_style = {}

app.layout = html.Div([
    # header
    html.Div([
        html.Div("Henry Pickersgill", className="heading_div"),
        html.Div("htap2@live.co.uk | 07470521144 | Cambridge, UK", className="heading_div"),
    html.Div(style={"height": "0.5rem", "background-color": "#172d4f"}),
        html.Div([
                html.A(f"{down_arrow} Home", id="home_link", className="navbar_link"),
                html.A(f"{right_arrow} Programming", id="programming_link", className="navbar_link"),
                html.A(f"{right_arrow} Piano", id="piano_link", className="navbar_link"),
                html.A(f"{right_arrow} Photography", id="photography_link", className="navbar_link")
            ],
                className="heading_div"
        ),
    html.Div(style={"height": "0.5rem", "background-color": "#172d4f"}),
    ]),

    # body
    html.Div([
        html.Div(style={"height": "0.5rem", "background-color": "#ffffff"}),
        html.Div(
            html.Div(
                [
                    html.B("About me", className="heading_18"),
                    f"{hollow_bullet} MPhys & BSc graduate from the University of Leeds",
                    html.Br(),
                    f"{hollow_bullet} Python developer",
                    html.Br(),
                    f"{hollow_bullet} Piano player",
                    html.Br(),
                    f"{hollow_bullet} Sports and fitness enthusiast",
                    html.Br(),
                    f"{hollow_bullet} Interested in many areas of Mathematics, Physics, Music and Technology",
                    html.Br(),
                    html.Br(),
                    html.B("Technical Experience", className="heading_18"),
                    html.B(f"{solid_bullet} Development Engineer at Toshiba Europe Ltd", className="heading_16"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),

                ],
                style=home_style,
                id="home_main_body"
            ),
            style={'background-color': '#ffffff'}
        ),
        html.Div("Programming contents here", id="programming_main_body", style={'display': 'none'}),
        html.Div("Piano contents here", id="piano_main_body", style={'display': 'none'}),
        html.Div("Photography contents here", id="photography_main_body", style={'display': 'none'}),
    ]),

    # footer
    html.Div([
        html.Footer("hello", style={'color': '#00ff00'})
    ], style={'position': 'relative'})
])

### CALLBACKS ###
@app.callback(
    Output("home_main_body", "style"),
    Output("programming_main_body", "style"),
    Output("piano_main_body", "style"),
    Output("photography_main_body", "style"),

    Output("home_link", "children"),
    Output("programming_link", "children"),
    Output("piano_link", "children"),
    Output("photography_link", "children"),

    Input("home_link", "n_clicks"),
    Input("programming_link", "n_clicks"),
    Input("piano_link", "n_clicks"),
    Input("photography_link", "n_clicks"),

    Input("home_link", "children"),
    Input("programming_link", "children"),
    Input("piano_link", "children"),
    Input("photography_link", "children"),
    prevent_initial_call=True
)
def show_hide_tabs(n_home, n_prog, n_piano, n_photo, home_div, prog_div, piano_div, photo_div):
    trigger = dash.callback_context.triggered[0]['prop_id']
    style_return_args = [st_none, ]*4
    div_return_args = [nop, nop, nop, nop]
    divs = [home_div, prog_div, piano_div, photo_div]
    styles = [home_style, prog_style, piano_style, photo_style]

    div_indices = {'home': 0, 'programming': 1, 'piano': 2, 'photography': 3}
    div_index = div_indices[trigger.split("_link")[0]]

    style_return_args[div_index] = styles[div_index]
    div_return_args[div_index] = change_arrow(divs[div_index], down_arrow)

    for i in range(4):
        if i != div_index:
            div_return_args[i] = change_arrow(divs[i], right_arrow)

    print(style_return_args)
    print(div_return_args)
    return *style_return_args, *div_return_args

def change_arrow(children, arrow):
    return f"{arrow} {children.split(' ')[1]}"

app.run_server(host='0.0.0.0', port=5000, debug=True)