from functools import wraps
from typing import Any, Callable, List
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

text = ["sugar", "yes, please", "DeanWinchester", "Castiel Novak", "SamWinchester"]


# 这里用了dash bootstrap component里的collapse 看不懂无所谓，只需要输出kwargs查看即可
def make_item(i):
    # we use this function to make the example items to avoid code duplication
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"Collapsible group #{i}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(f"This is the content of group {i}..{text[i]}"),
                id=f"collapse-{i}",
            ),
        ]
    )


accordion = html.Div(
    [make_item(i) for i in range(1, 5)], className="accordion"
)
app.layout = html.Div(
    [accordion]
)


def dash_kwarg(inputs):
    def accept_func(func):
        @wraps(func)
        def wrapper(*args):
            input_names = [item.component_id for item in inputs]
            kwargs_dict = dict(zip(input_names, args))
            return func(**kwargs_dict)

        return wrapper

    return accept_func


# inputs = [Input("plot-button", "n_clicks")]

# states = [[State('input1', 'on'), State('input2','value'), State('input22','value')]]
length = 5
outputs = [Output(f"collapse-{i}", "is_open") for i in range(1, 5)]
inputs = [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 5)]
states = [State(f"collapse-{i}", "is_open") for i in range(1, 5)]


@app.callback(
    outputs,
    inputs,
    states,
)
@dash_kwarg(inputs + states)
def generate_graph(**kwargs):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ""
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    print(button_id)
    print(kwargs)
    i = 0
    ans = []
    for arg in kwargs:
        i = i + 1
        if i <= (length - 1):
            if arg == button_id:
                v = kwargs[button_id]
                if v == None:
                    ans.append(False)
                elif v % 2 == 0:
                    ans.append(False)
                else:
                    ans.append(True)
            else:
                ans.append(False)
        else:
            break
    return ans


if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
