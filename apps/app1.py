import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import pandas as pd
from app import app
import dash_bootstrap_components as dbc

material_list = ['1', '2', '3']
layout = html.Div([

    dbc.RadioItems(
        id='my_degree',
        options=[
            {'label': material_list[0], 'value': '1'},
            {'label': material_list[1], 'value': '2'},
            {'label': material_list[2], 'value': '3'}
        ],
        value='3', labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='dcc_store_compoenent_id')
])


@app.callback(
    Output('dcc_store_compoenent_id', 'data'),
    [Input('my_degree', 'value')])
def store_slider_value_in_dcc_store(slider_value):
    return {'slider_app1_value': slider_value}
