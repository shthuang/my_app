import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash
import prepare_web as pw

global num, st_information
num = 10
st_information = {}


def f1(s):
    return dcc.Markdown(str(s))


def fun(st_id, class_id):
    global st_information
    st_information['st_id'] = st_id
    st_information['class_id'] = class_id


def student_part():
    global st_information
    st_information = {}

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

    @app.callback(Output(component_id='class_id', component_property='children'),
                  [Input(component_id='my_id', component_property='value'),
                   Input(component_id='my_class', component_property='value')])
    def student_data(st_id, class_id):
        print([st_id, class_id])
        fun(st_id, class_id)
        print([st_id, class_id, st_information])
        return str([st_id, class_id])

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

    @app.callback(
        Output(component_id='st_degree', component_property='children'),
        [Input(component_id='my_degree', component_property='value')]
    )
    def update_output_div1(degree):
        global st_information
        st_information['st_degree'] = degree
        print(st_information)
        return dcc.Markdown(str([degree, st_information]))

    return layout


if __name__ == '__main__':

    app = dash.Dash(suppress_callback_exceptions=True)
    server = app.server
    app.config.suppress_callback_exceptions = True
    app.title = 'my-dash-multi-page-app'

    app.layout = html.Div([
        html.H2(children='my-app-is-running', id='title'),

        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])

    # 目录页
    index_page = html.Div([
        html.H4(children='请选择身份：'),
        html.Ul([
            html.Li(html.A('student', href='student')),
            html.Li(html.A('teacher', href='teacher')),
        ]),

    ])

    # Update the index
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        global st_information
        print('display_page ' + pathname)
        if pathname == '/':
            return index_page
        elif pathname == '/student':
            layout = student_part()
            return layout
        elif pathname == '/teacher':
            return teacher_part()

        elif pathname == '/student/t0':
            return student_read_material()
        elif pathname == '/student/t1':
            print('这次可以吗' + str(st_information))
            return f1(str(st_information))
        # elif pathname == '/student/t3':
        #     return f1(pathname)
        # elif pathname == '/student/t4':
        #     return f1(pathname)


    app.run_server(debug=True)
    print(st_information)



