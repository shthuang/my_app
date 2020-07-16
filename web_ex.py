# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:29:26 2019

@author: 17968
"""
import dash
import dash_core_components

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output 



app = app = dash.Dash()
app.add_external_link = False
app.layout = html.Div([
    html.H2('选项卡示例', style = dict(textAlign='center')),
    dcc.Tabs(
        id = 'tabs-example',
        value = 'tab-1',
        children = [dcc.Tab(label = '选项卡一', value = 'tab-1'),
                    dcc.Tab(label = '选项卡二', value = 'tab-2')]),
    html.Div(id = 'tabs-demo')
])

@app.callback(Output('tabs-demo', 'children'), [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('内容一'),
            dcc.Graph(
                id='graph-1-tabs',
                figure = dict(data = [dict(x = [1, 2, 3], y = [3, 1, 2], type = 'bar')])
            )
        ])
    else:
        return html.Div([
            html.H3('内容二'),
            dcc.Graph(
                id='graph-2-tabs',
                figure = dict(data = [dict(x = [1, 2, 3], y = [5, 10, 6], type = 'bar')])
            )
        ])

app.run_server(debug=False)
































