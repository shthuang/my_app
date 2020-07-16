import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import prepare_web as pw


def fun():
    List = [html.H4('这样可以吗?'),
            dcc.RadioItems(className='radio-items', id='test3',
                           options=[
                                {'label': '测试1', 'value': 'on'},
                                {'label': '测试2', 'value': 'off'},
                                {'label': '测试3', 'value': '3'}
                            ],  value='on')
            ]
    return List


df = pw.class_st_table('002')
div, fig_list = pw.generate_table(df)

app = dash.Dash('example')

app.layout = html.Div([
    html.Div([div] + fig_list),
    dcc.Dropdown(
        id='dropdown-to-show_or_hide-element',
        options=[
            {'label': 'Show element', 'value': 'on'},
            {'label': 'Hide element', 'value': 'off'},
            {'label': '3 element', 'value': '3'},
            {'label': '2 element', 'value': '2'}
        ],
        value='on'
    ),

    # Create Div to place a conditionally visible element inside
    html.Div([
        # Create element to hide/show, in this case an 'Input Component'
        dcc.Input(id='element-to-hide', placeholder='something', value='Can you see me?')
    ], style={'display': 'none'}  # <-- This is the line that will be changed by the dropdown callback
    ),
    html.Div(id='test',
             children=[
                # Create element to hide/show, in this case an 'Input Component'
                html.H4('这样可以吗'),
                dcc.Input(id='element-to-hide3', placeholder='something', value='Can you see me3?'),
                dcc.Input(id='element-to-hide3_1', placeholder='something', value='Can you see me3_1?'),
                dcc.Dropdown(
                        id='test2',
                        options=[
                            {'label': '1', 'value': 'on'},
                            {'label': '2', 'value': 'off'},
                            {'label': '3', 'value': '3'}
                        ],
                        value='on')
                       ],
             style={'display': 'block'}  # <-- This is the line that will be changed by the dropdown callback
             ),
    dcc.Dropdown(
        id='dropdown-to-show_or_hide-element2',
        options=[
            {'label': 'Show element', 'value': 'on'},
            {'label': 'Hide element', 'value': 'off'},
            {'label': '3 element', 'value': '3'}
        ],
        value='on', style={'display': 'none'}
    ),

    html.Div(id='result', children=[
        dcc.RadioItems(id='choose')
    ]),

    html.Div(id='my_test',
             children=fun(),
             style={'display': 'block'}  # <-- This is the line that will be changed by the dropdown callback
             ),
    html.Div(id='output')

    ])


@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_element1(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}


@app.callback(
   Output(component_id='dropdown-to-show_or_hide-element2', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_element2(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == '3':
        return {'display': 'none'}


@app.callback(
   Output(component_id='test', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
def show_hide_element3(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@app.callback(
   Output(component_id='result', component_property='children'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value'),
    Input(component_id='element-to-hide', component_property='value'),
    Input(component_id='element-to-hide3', component_property='value'),
    Input(component_id='element-to-hide3_1', component_property='value'),
    Input(component_id='dropdown-to-show_or_hide-element2', component_property='value')])
def show_hide_element4(v1, v2, v3, v4, v5):
    return dcc.RadioItems(id='choose',
                          options=[
                              {'label': 'question_dict[0][key][0]', 'value': '1'},
                              {'label': 'question_dict[0][key][1]', 'value': '2'},
                              {'label': 'question_dict[0][key][2]', 'value': '3'}
                          ])


@app.callback(Output(component_id='output', component_property='children'),
              [Input(component_id='choose', component_property='value')])
def update(v):
    return str(v)


if __name__ == '__main__':
    app.run_server(debug=True)

