import dash
from dash import Output, Input, State
from dash import html
from dash import dcc
import sys

app = dash.Dash(__name__)
server = app.server

right_arrow = "\u25b8"
down_arrow = "\u25be"
hollow_bullet = "\u25e6"
solid_bullet = "\u2022"

st_block = {"display": "block"}
st_none = {"display": "none"}
nop = dash.no_update

app.layout = html.Div([
    # header
    html.Div([
        html.Div([
            html.Div("Henry Pickersgill", style={"margin-left": "41.5rem", "display": "inline-block"}),
            html.Div("", style={"width": "38.5rem", "display": "inline-block"}),
            html.Button(
                html.Div(className="dark_mode_inner"),
                id="dark_mode_btn",      
                className="dark_mode_btn")
            ], id="name", className="top_heading_div"),
        html.Div("htap2@live.co.uk | 07470521144 | Cambridge, UK", className="heading_div"),
    ]),

    # sticky header
    html.Div([
        html.Div(style={"height": "0.5rem", "background-color": "#172d4f"}),
        html.A(f"{down_arrow} Profile", id="home_link", className="navbar_link"),
        html.A(f"{right_arrow} Programming", id="programming_link", className="navbar_link"),
        html.A(f"{right_arrow} Piano", id="piano_link", className="navbar_link"),
        html.A(f"{right_arrow} Photography", id="photography_link", className="navbar_link"),
        html.Div(style={"height": "0.5rem", "background-color": "#172d4f"}),
    ], className="heading_div", style={"position": "sticky", "top": "0"}),

    # body
    html.Div([
        html.Div(id="top_content_v_spacer", className="white_v_spacer"),
        html.Div([
            ### HOME TAB
            html.Div(
                [
                    html.B("About me",className="heading_18"),
                    html.Div(
                        [
                            f"{hollow_bullet} MPhys & BSc graduate from the University of Leeds",
                            html.Div("", style={"height": "0.5rem"}),
                            f"{hollow_bullet} Python developer",
                            html.Div("", style={"height": "0.5rem"}),
                            f"{hollow_bullet} Piano player",
                            html.Div("", style={"height": "0.5rem"}),
                            f"{hollow_bullet} Sports and fitness enthusiast",
                            html.Div("", style={"height": "0.5rem"}),
                            f"{hollow_bullet} Interested in many areas of Mathematics, Physics, Music and Technology",
                            html.Div("", style={"height": "0.5rem"}),
                    ], className="list_item"),
                    html.Br(),
                    html.B("Technical Experience", className="heading_18"),
                    html.B(f"{solid_bullet} Development Engineer at Toshiba Europe Ltd, Cambridge (2 years 2 months)", className="heading_16"),
                    html.Div([
                        f"{hollow_bullet} Responsible for the development and test of Quantum Key Distribution systems (see ",
                        html.A(
                            "what is QKD?)",
                            href="https://www.techtarget.com/searchsecurity/definition/quantum-key-distribution-QKD",
                            target="_blank",
                            id="what_is_qkd_link",
                            style={"color": "#0000ff"}
                        ),
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Lead developer in self-conceived automation project: large-scale front and back-end Python tool "
                        "for automating the test and optimisation of QKD systems. Designed to speed up and simplify the test/optimisation procedures",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Maintainer and developer of C++ control code and Linux control servers, including development of new algorithms and maintenance of PID loops",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Supervised other members of the team and distributed automation project tasks according to the team members' experience with Python",
                    ], className="list_item"),
                    html.Br(),
                    html.B("Technical interests", className="heading_18"),
                    html.Div([
                        f"{hollow_bullet} Research science",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Python development for automation",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Game and physics engine development",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Electronics (e.g., Arduino), computers and other hardware",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} 3D design for 3D printing",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Mathematical simulations, algorithms and general problem solving",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Windows and Android app development",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} Music notation software and audio analysis",
                        
                    ], className="list_item"),
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
                className="content",
                id="home_main_body"
            ),
            ### PROGRAMMING TAB
            html.Div(
                [
                    html.B("My approach to software development", className="heading_18"),
                    html.Div([
                        f"{hollow_bullet} My journey with programming began at Leeds University during my Physics degree. During this degree, Python was ",
                        "used for data analysis, plotting and testing of physical models (i.e., through curve fitting to equations generated by a particular model). ",
                        "I quickly became interested in Python and software in general.",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} During my time at Toshiba Europe Ltd, I became the lead developer in an automation project. The aim was to test and ",
                        "optimise QKD systems - before I joined the team this was almost completely manual. This automation project contained approximately 20 Python scripts, all designed ",
                        "to optimise one part of the electronics/optics contained within the system. This project also contained a front-end so I became familiar with front-end "
                        "development and best-practices. This tool is now the main method of testing the QKD systems and is used by staff unfamiliar with the inner workings of the system.",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} I write clean, concise and well-commented code and I am particularly careful with repeated code. ",
                        html.Div("", style={"height": "0.5rem"}),
                        f"{hollow_bullet} I explore programming outside of work, including trying other languages - please see below."
                    ], className="list_item"),
                    html.Br(),                    
                    html.B("Python", className="heading_18"),
                    html.B(f"{solid_bullet} 2D game development", className="heading_16"),
                    html.Div([
                        html.Div(f"{hollow_bullet} ", style={"display": "inline-block"}), 
                        html.A(" Brickbreaker", id="brick_link", href="https://github.com/Henryp1997/brickbreak", target="_blank", className="github_link"),
                        " - 2D paddle and ball game where the objective is to break all the bricks on the screen. No online game development resources "
                        "were used aside from the 2D engine (pygame) documentation, as a challenge for myself. Below you can see a screenshot of the third level, with multiple powerups active.",
                        html.Div("", style={"height": "0.5rem"}),
                        html.Div(
                            html.Img(src="./assets/screenshots/brickbreak.png", style={"height": "50%", "width": "50%"}),
                            style={"text-align": "center"}
                        ),
                        html.Div("", style={"height": "0.5rem"}),
                        html.Div(f"{hollow_bullet} ", style={"display": "inline-block"}),
                        html.A(" Platformer", id="platformer_link", href="https://github.com/Henryp1997/platformer", target="_blank", className="github_link"),
                        " - Began experimenting with 2D platform game physics. Not using any online resources to work out the dynamics of the player's movements, "
                        "aside from the 2D engine (pygame) documentation, as a challenge for myself. This project is in the early stages. Below you can see a screenshot of the demo "
                        "which currently allows the player to walk and interact with platforms.",
                        html.Div("", style={"height": "0.5rem"}),
                        html.Div(
                            html.Img(src="./assets/screenshots/platformer.png", style={"height": "50%", "width": "50%"}),
                            style={"text-align": "center"}
                        ),
                        html.Div("", style={"height": "0.5rem"}),
                        html.Div(f"{hollow_bullet} ", style={"display": "inline-block"}),
                        html.A(" Conway's game of life", id="GoL_link", href="https://github.com/Henryp1997/Game-of-life", target="_blank", className="github_link"),
                        " - Implementation in Python. This was my first experience with 'game' development and I added some nice-to-have features "
                        "such as the ability to click cells to 'resurrect' dead cells and start with unique patterns. Below you can see a demonstration of the so-called 'Glider gun' pattern.",
                        html.Div("", style={"height": "0.5rem"}),
                        html.Div(
                            html.Img(src="./assets/screenshots/game_of_life.png", style={"height": "50%", "width": "50%"}),
                            style={"text-align": "center"}
                        ),
                    ], className="list_item"),
                    html.B(f"{solid_bullet} Automation"),
                    html.Div([
                        
                    ]),
                    html.Br(),
                    html.B("Web development with HTML, CSS and JS", className="heading_18"),
                    html.Div([
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                    ], className="list_item"),
                    html.Br(),
                    html.B("Garmin watch face creation (Monkey C)", className="heading_18"),
                    html.Div([
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                    ], className="list_item"),
                    html.Br(),
                    html.B("C++", className="heading_18"),
                    html.Div([
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                        "test",
                        html.Div("", style={"height": "0.5rem"}),
                    ], className="list_item")
                ],
                className="display_none",
                id="programming_main_body"
            ),
            ### PIANO TAB
            html.Div(id="piano_main_body", className="display_none"),
            ### PHOTOGRAPHY TAB
            html.Div(id="photography_main_body", className="display_none"),
        ], id="content_borders", className="content_border")
    ]),

    html.Div([
        html.Div(id="percentage_bar", style={"background-image": "linear-gradient(to right, #116927 0%, #ffffff 0%)", "background-color": "#ffffff", "height": "0.5rem"}),
    ], style={"position": "sticky", "bottom": "0"}),

    # hidden divs
    html.Div(style=st_none, id="hidden_div1"),
    html.Div(style=st_none, id="hidden_div2"),
    html.Div(style=st_none, id="hidden_div3"),
    # dcc.Interval(interval=100, id="mobile_interval")
])

### CALLBACKS ###
@app.callback(
    Output("home_main_body", "className"),
    Output("programming_main_body", "className"),
    Output("piano_main_body", "className"),
    Output("photography_main_body", "className"),

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
    State("dark_mode_btn", "n_clicks"),
    prevent_initial_call=True
)
def show_hide_tabs(n_home, n_prog, n_piano, n_photo, home_div, prog_div, piano_div, photo_div, n_dark):
    trigger = dash.callback_context.triggered[0]['prop_id']
    classnames = ["display_none",]*4
    div_return_args = [nop, nop, nop, nop]
    divs = [home_div, prog_div, piano_div, photo_div]

    div_indices = {'home': 0, 'programming': 1, 'piano': 2, 'photography': 3}
    div_index = div_indices[trigger.split("_link")[0]]

    classnames[div_index] = "content_dark"
    if n_dark is None or n_dark % 2 == 0:
        classnames[div_index] = "content"

    div_return_args[div_index] = change_arrow(divs[div_index], down_arrow)

    for i in range(4):
        if i != div_index:
            div_return_args[i] = change_arrow(divs[i], right_arrow)

    return *classnames, *div_return_args

def change_arrow(children, arrow):
    return f"{arrow} {children.split(" ")[1]}"

app.clientside_callback(
""" function (n1, n2, n3, n4) {
        if (n1 || n2 || n3 || n4) {
            window.scrollTo(0, 0)
        }
    }
""",
    Output('hidden_div1', 'children'),
    Input('home_link', 'n_clicks'),
    Input('programming_link', 'n_clicks'),
    Input('piano_link', 'n_clicks'),
    Input('photography_link', 'n_clicks')
)

# app.clientside_callback(
# """ function (n) {
#     if (n) {
#         pass
#         }
#     }
# }
# """,
#     Output('hidden_div2', 'children'),
#     Input('mobile_interval', 'n_intervals')
# )

# @app.callback(
#     Output('mobile_interval', 'disabled'),
#     Input('mobile_interval', 'n_intervals'),
#     prevent_initial_call=True
# )
# def disable_mobile_check_interval(n):
#     if n > 0:
#         return True
#     return False

@app.callback(
    Output("home_main_body", "className", allow_duplicate=True),
    Output("programming_main_body", "className", allow_duplicate=True),
    Output("piano_main_body", "className", allow_duplicate=True),
    Output("photography_main_body", "className", allow_duplicate=True),
    Output("top_content_v_spacer", "className"),
    Output("content_borders", "className"),

    Output("what_is_qkd_link", "style"),
    Output("brick_link", "style"),
    Output("platformer_link", "style"),
    Output("GoL_link", "style"),

    Input("dark_mode_btn", "n_clicks"),
    State("home_main_body", "className"),
    State("programming_main_body", "className"),
    State("piano_main_body", "className"),
    State("photography_main_body", "className"),
    prevent_initial_call=True
)
def toggle_dark_mode(n, home_class, prog_class, piano_class, photo_class):
    style_dict = {
        0: ("content", ["white_v_spacer", "content_border", *({'color': '#0000ff'},)*4]),
        1: ("content_dark", ["black_v_spacer", "content_border_dark", *({'color': '#00ff00'},)*4])
    }
    classes = ["display_none",]*4
    for i, classname in enumerate([home_class, prog_class, piano_class, photo_class]):
        if classname != "display_none":
            classes[i] = style_dict[n % 2][0]
            break
    return *classes, *style_dict[n % 2][1]
    

if __name__ == "__main__":
    # app.run_server(host='0.0.0.0', port=5000, debug=True if int(sys.argv[1]) == 1 else False)
    app.run_server()