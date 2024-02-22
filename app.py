import dash
from dash import Output, Input, State
from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

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
    'background-color': '#f4f4f4',
    'color': 'black',
    'font-family': 'Open-Sans',
    'width': '70%',
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
    ]),

    # sticky header
    html.Div([
            html.Div(style={"height": "0.3rem", "background-color": "#172d4f"}),
            html.A(f"{down_arrow} Home", id="home_link", className="navbar_link"),
            html.A(f"{right_arrow} Programming", id="programming_link", className="navbar_link"),
            html.A(f"{right_arrow} Piano", id="piano_link", className="navbar_link"),
            html.A(f"{right_arrow} Photography", id="photography_link", className="navbar_link"),
            html.Div(style={"height": "0.3rem", "background-color": "#172d4f"}),
        ],
            className="heading_div", style={'position': 'sticky', 'top': '0'}),

    # body
    html.Div([
        html.Div(style={"height": "0.5rem", "background-color": "#ffffff"}),
        html.Div(
            html.Div(
                [
                    html.B("About me", className="heading_18"),
                    html.Div(f"{hollow_bullet} MPhys & BSc graduate from the University of Leeds", className="list_item"),
                    html.Div(f"{hollow_bullet} Python developer", className="list_item"),
                    html.Div(f"{hollow_bullet} Piano player", className="list_item"),
                    html.Div(f"{hollow_bullet} Sports and fitness enthusiast", className="list_item"),
                    html.Div(f"{hollow_bullet} Interested in many areas of Mathematics, Physics, Music and Technology", className="list_item"),
                    html.Br(),
                    html.B("Technical Experience", className="heading_18"),
                    html.B(f"{solid_bullet} Development Engineer at Toshiba Europe Ltd", className="heading_16"),
                    html.Div([
                        f"{hollow_bullet} Responsible for the development and test of Quantum Key Distribution systems (see ",
                        html.A("what is QKD?)", href="https://www.techtarget.com/searchsecurity/definition/quantum-key-distribution-QKD", target="_blank", style={"color": "#0000ff"})
                    ], className="list_item"),
                    html.Div(f"{hollow_bullet} Lead developer in self-conceived automation project: large-scale front and back-end Python tool"
                             "for automating the test and optimisation of QKD systems. Designed to speed up and simplify the test/optimisation procedures", className="list_item"),
                    html.Div(f"{hollow_bullet} Maintainer and developer of C++ control code and Linux control servers, including development of new algorithms and maintenance of PID loops", className="list_item"),
                    html.Div(f"{hollow_bullet} Supervised other members of the team and distributed automation project tasks according to the team members' experience with Python", className="list_item"),
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
        html.Div([
            html.Div(["hello", html.Br()]),
            ] * 100
            , id="programming_main_body", style={'display': 'none'}),
        html.Div([
            html.Div(["hello", html.Br()]),
            ] * 100
            , id="piano_main_body", style={'display': 'none'}),
        html.Div([
            html.Div(["hello", html.Br()]),
            ] * 100
            , id="photography_main_body", style={'display': 'none'}),
    ]),

    html.Div([
        html.Div(id="percentage_bar", className="percentage_bar", style={'background-image': 'linear-gradient(to right, #116927 0%, #ffffff 0%)', 'background-color': '#ffffff', "height": "0.5rem"}),
    ], style={"position": "sticky", "bottom": "0"}),

    # hidden divs
    html.Div("test", style=st_none, id="hidden_div1"),
    html.Div(style=st_none, id="hidden_div2"),
    html.Div(style=st_none, id='hidden_div3'),
    dcc.Interval(interval=500, id="percentage_bar_timer")
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

app.clientside_callback(
""" function (n1, n2, n3, n4) {
        if (n1 || n2 || n3 || n4) {
            window.scrollTo(0, 0)
        }
    }
""",
    Output('hidden_div3', 'children'),
    Input('home_link', 'n_clicks'),
    Input('programming_link', 'n_clicks'),
    Input('piano_link', 'n_clicks'),
    Input('photography_link', 'n_clicks')
)

app.run_server(host='0.0.0.0', port=5000, debug=True)