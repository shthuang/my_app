import pandas as pd
import dash_core_components as dcc   #引入dash核心元素
import dash_html_components as html   #引入dash html元素
from app import app
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc

material_list = ['12', '22', '32']
layout = html.Div([

    dbc.RadioItems(
        id='my_d2',
        options=[
            {'label': material_list[0], 'value': '1'},
            {'label': material_list[1], 'value': '2'}
        ],
        value='3', labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='the_output')
])


@app.callback(
    Output(component_id='the_output', component_property='children'),
    [Input('whatever', 'you_want')],
    [State('dcc_store_compoenent_id', 'data')])
def func(input_value, data):
    slider_value = data['slider_app1_value']
    print(slider_value)
    return dcc.Markdown(str(slider_value))
