from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

my_input = dcc.Input(value = 'initial_value', type = 'text')
my_output = html.Div()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!")
    html.Div([
        "Input: ",
        dcc.Input(id = "my-input", value = "intial-value", type = "text")
    ]),
    html.Br(),
    html.Div(id = "my-output"),
])