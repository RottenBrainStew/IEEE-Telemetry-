# Run this app with "python.app.py" and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),
        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'],
                ['Montreal', 'San Francisco'],
                multi = True),
        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),
    ], style = {'padding': 10, 'flex': 1}),
    html.Div(children = [
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montreal', 'San Francisco'],
                    ['Montreal', 'San Francisco']
        ),
        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value = "MTL", type = "text"),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min = 0,
            max = 9,
            marks = {i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == "__main__":
    app.run_server(debug = True, port = 8053) #Manually set the port you need to