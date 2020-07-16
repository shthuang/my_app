import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash
import prepare_web as pw


def student_part():

    layout = html.Div([

        html.H3(children='个人信息填写'),
        html.H4(children='请输入学号：'),
        dcc.Input(id='my_id', value='19213066', type='text',
                  style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
        html.Div(id='st_id'),

        html.H4(children='请输入班号：'),
        dcc.Input(id='my_class', value='007', type='text',
                  style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
        html.Div(id='class_id'),

        # dcc.Location(id='url_student', refresh=False),
        html.Ul([
            html.Li(html.A('开始测试', href='student/t0'))
        ]),
        # html.Div(id='page-content0'),
    ])

    return layout


def teacher_part():
    layout = html.Div([
        html.H3(children='个人信息填写'),
        html.H4(children='请输入教职工号：'),
        dcc.Input(id='my-id', value='19213', type='text',
                  style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
        html.Div(id='st_id'),

        dcc.Location(id='url2', refresh=False),
        html.Ul([
            html.Li(html.A('上一题', href='/app1/t1')),
            html.Li(html.A('下一题', href='/app1/t2'))
        ]),
        html.Div(id='page-content2'),
    ])

    @app.callback(
        Output(component_id='st_id', component_property='children'),
        [Input(component_id='my-id', component_property='value')]
    )
    def update_output_div0(input_value1):
        text = 'ok!' + '\t' + str(input_value1)
        return dcc.Markdown(text)

    return layout


def student_read_material():
    # 阅读材料加载
    read_material_text = pw.create_read_material().replace('1、', '#').replace('2、', '#').replace('3、', '#')\
        .replace('\u3000', '').split('#')
    material_list = []
    for line in read_material_text:
        if line != '':
            material_list.append(line)
    layout = html.Div([
        html.H4(children='请选择最合适你阅读的材料：'),
        # 单选题
        dbc.RadioItems(
            id='my_degree',
            options=[
                {'label': material_list[0], 'value': '1'},
                {'label': material_list[1], 'value': '2'},
                {'label': material_list[2], 'value': '3'}
            ],
            value='3', labelStyle={'display': 'inline-block'}
        ),
        html.Div(id='st_degree'),

        html.Ul([
            html.Li(html.A('下一题', href='/student/t1'))
        ]),
    ])

    return layout


def load_read_material():
    read_material_text = pw.create_read_material().replace('1、', '#').replace('2、', '#').replace('3、', '#')\
        .replace('\u3000', '').split('#')
    material_list = []
    for line in read_material_text:
        if line != '':
            material_list.append(line)
    return material_list


if __name__ == '__main__':
    global st_data, materials
    st_data = {}
    materials = load_read_material()

    app = dash.Dash(suppress_callback_exceptions=True)
    server = app.server
    app.config.suppress_callback_exceptions = True
    app.title = 'my-dash-multi-page-app'

    app.layout = html.Div([
        html.H2(children='my-app-is-running', id='title'),

        html.Div(id='input_role',
                 children=dbc.RadioItems(
                    id='my_role',
                    options=[
                        {'label': 'student', 'value': 'student'},
                        {'label': 'teacher', 'value': 'teacher'}
                    ]
                    ), style={'display': 'block'}
                 ),
        # html.Div(id='page-content'),

        # 学生模块
        html.Div(id='text1', children=[html.H2('个人信息填写')], style={'display': 'none'}),
        html.Div(id='text2', children=[html.H4('请输入学号：')], style={'display': 'none'}),
        html.Div(id='st_id_input',
                 children=[dcc.Input(id='my_id', value='19213066', type='text',
                           style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
                           html.Div(id='st_id'),
                           ], style={'display': 'none'}),
        html.Div(id='text3', children=[html.H4('请输入班级：')], style={'display': 'none'}),
        html.Div(id='st_class_input',
                 children=[dcc.Input(id='my_class', value='007', type='text',
                           style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
                           html.Div(id='class_id')],
                 style={'display': 'none'}),

        dcc.Markdown('\n****************\n'),

        html.Button('开始测试', id='button', style={'display': 'none'}),

        html.Div(id='text4', children=[html.H4('请选择最合适你阅读的材料：')], style={'display': 'none'}),
        dbc.RadioItems(id='my_degree',
                       options=[
                            {'label': materials[0], 'value': '1'},
                            {'label': materials[1], 'value': '2'},
                            {'label': materials[2], 'value': '3'}
                        ],
                       value='3', style={'display': 'none'}
                       ),
        html.Button('下一题', id='button_t1', style={'display': 'none'}),


        html.Button('下一题', id='button_t2', style={'display': 'none'}),
        html.Button('下一题', id='button_t3', style={'display': 'none'}),
        html.Button('下一题', id='button_t4', style={'display': 'none'}),
        html.Button('下一题', id='button_t5', style={'display': 'none'}),
        html.Button('下一题', id='button_t6', style={'display': 'none'}),
        html.Button('下一题', id='button_t7', style={'display': 'none'}),
        html.Button('下一题', id='button_t8', style={'display': 'none'}),
        html.Button('下一题', id='button_t9', style={'display': 'none'}),
        html.Button('下一题', id='button_t10', style={'display': 'none'}),
        html.Button('提交结果', id='button_end', style={'display': 'none'}),


        html.Div(id='output'),
    ])

    # 选择角色之后，激活学生模块
    @app.callback([Output(component_id='text1', component_property='style'),
                   Output(component_id='text2', component_property='style'),
                   Output(component_id='st_id_input', component_property='style'),
                   Output(component_id='text3', component_property='style'),
                   Output(component_id='st_class_input', component_property='style'),
                   Output(component_id='button', component_property='style'),
                   Output(component_id='my_degree', component_property='style')],
                  [Input(component_id='my_role', component_property='value'),
                   Input(component_id='button', component_property='n_clicks')])
    def display_page(role, n_clicks):
        print(role)
        if role == 'student' and n_clicks is None:
            return [{'display': 'block'}]*7
        elif role != 'student' and n_clicks is None:
            return [{'display': 'none'}]*7
        elif role == 'student' and n_clicks is not None:
            return [{'display': 'none'}]*5 + [{'display': 'block'}]*2
        else:
            return [{'display': 'none'}]*7

    # 开始测试之后，只留下题目的显示
    # @app.callback([Output(component_id='text1', component_property='style'),
    #                Output(component_id='text2', component_property='style'),
    #                Output(component_id='st_id_input', component_property='style'),
    #                Output(component_id='text3', component_property='style'),
    #                Output(component_id='st_class_input', component_property='style'),
    #                Output(component_id='button', component_property='style')],
    #               [Input(component_id='button', component_property='n_clicks')])
    # def display_page(n_clicks):
    #     if n_clicks is not None and n_clicks >= 1:
    #         return [{'display': 'none'}] * 6
        # else:
        #     return [{'display': 'block'}] * 7

    # Update the st_data
    @app.callback(Output(component_id='output', component_property='children'),
                  [Input(component_id='my_id', component_property='value'),
                   Input(component_id='my_class', component_property='value'),
                   Input(component_id='my_degree', component_property='value')])
    def display_page(my_id, my_class, degree):
        st_data['st_id'] = my_id
        st_data['class'] = my_class
        st_data['st_degree'] = degree
        print(st_data)
        return dcc.Markdown(str(st_data))

    app.run_server(debug=True)



