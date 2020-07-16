import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import prepare_web as pw


# 阅读材料加载
read_material_text = pw.create_read_material()
# 模块字典
global num
num = 10

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H3(children='个人信息填写'),
    html.H4(children='请输入学号：'),
    dcc.Input(id='my-id', value='19213', type='text',
              style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
    html.Div(id='st_id'),

    html.H4(children='请输入年级：'),
    dcc.Input(id='my-grade', value='2', type='text',
              style={'width': '25%', "margin-left": "auto", "margin-right": "auto"}),
    html.Div(id='st_grade'),

    dcc.Markdown(children='************************'),
    html.H6(children='以下哪段文字更符合你的阅读水平？'),
    dcc.Markdown(children=read_material_text),
    dcc.Markdown(children='**请输入答案：**'),
    dcc.Input(id='degree', type='text', value='2'),
    html.Div(id='st_degree'),

    # 出题模块
    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q0_answer', type='text', value='A,D'),
    html.Div(id='st_q0_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q1_answer', type='text', value='C,D'),
    html.Div(id='st_q1_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q2_answer', type='text', value='A,B'),
    html.Div(id='st_q2_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q3_answer', type='text', value='A,C'),
    html.Div(id='st_q3_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q4_answer', type='text', value='C,B'),
    html.Div(id='st_q4_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q5_answer', type='text', value='A,A'),
    html.Div(id='st_q5_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q6_answer', type='text', value='C,D'),
    html.Div(id='st_q6_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q7_answer', type='text', value='D,A'),
    html.Div(id='st_q7_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q8_answer', type='text', value='C,D'),
    html.Div(id='st_q8_answer'),

    dcc.Markdown(children='**请输入答案（用逗号分隔）：**'),
    dcc.Input(id='q9_answer', type='text', value='C,D'),
    html.Div(id='st_q9_answer'),

    # 反馈模块
    dcc.Markdown(children='************************'),
    html.H3(children='阅读反馈'),
    html.H4(children='请输入书名或者文章名：'),
    dcc.Input(id='my-book', value='灰天鹅作文350字', type='text'),
    html.Div(id='st_book'),

    html.H4(children='该书（文章）你掌握了多少？'),
    # dcc.Input(id='my-reaction', value='太简单', type='text'),
    # 这里应该修改为读懂了多少百分比
    dcc.Dropdown(id='my-reaction', options=[
        {'label': '100%', 'value': '100'},
        {'label': '80%', 'value': '80'},
        {'label': '60%', 'value': '60'},
        {'label': '40%', 'value': '40'},
        {'label': '20%', 'value': '20'},
        {'label': '0%', 'value': '0'}
    ], value='', style={'width': '50%'}),
    html.Div(id='st_reaction'),

    html.H4(children='请输入喜欢的文案：'),
    dcc.Input(id='txt', type='text', value='我的奶奶是一个特别勤劳的人，她特别喜欢养鸭子，这次她养了一只“灰天鹅”。'
                                           '奶奶告诉我说“灰天鹅”最喜欢吃青草了，从小就长得特别特别的快，到现在已经很大很大了，'
                                           '比一般的鸭子都要大的多。我弟弟今年3岁了，他还没上幼儿园，整天跟在奶奶后面跟鸭子们玩游戏，'
                                           '他最喜欢追着“灰天鹅”满地里跑。有一天我突然听到了“灰天鹅”大叫的声音，我跑出去一看，'
                                           '原来是弟弟又在追“灰天鹅”了，我看见“灰天鹅”跑得时候整个圆鼓鼓的身子是一扭一扭的，'
                                           '两只大脚掌用力地拍打着地面，还发出了“扑哒”“扑哒”的声音，脖子伸的长长得头望着天空用力的'
                                           '叫着“鹅，鹅，鹅”，翅膀完全打开用力地扇着，感觉“灰天鹅”想要往天上飞一样，可是又飞不上去，'
                                           '只能满地跑来跑去找地方躲，看着“灰天鹅”跑起来的样子说多搞笑就有多搞笑，'
                                           '我和弟弟看着一起哈哈大笑了起来！',
              autoFocus='autoFocus', style={'text-align': 'center', 'width': '250px', 'padding': '5px 5px',
                                            'margin': 'auto'}),
    html.Div(id='st_txt'),
])


@app.callback(
    Output(component_id='st_degree', component_property='children'),
    [Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div0(input_value1, input_value2):
    q_index = 0
    st_id, degree = input_value1, input_value2
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    # print(text)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q0_answer', component_property='children'),
    [Input(component_id='q0_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div1(input_value1, input_value2, input_value3):
    q_index = 1
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q1_answer', component_property='children'),
    [Input(component_id='q1_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div2(input_value1, input_value2, input_value3):
    q_index = 2
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q2_answer', component_property='children'),
    [Input(component_id='q2_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div3(input_value1, input_value2, input_value3):
    q_index = 3
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q3_answer', component_property='children'),
    [Input(component_id='q3_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div4(input_value1, input_value2, input_value3):
    q_index = 4
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q4_answer', component_property='children'),
    [Input(component_id='q4_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div5(input_value1, input_value2, input_value3):
    q_index = 5
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q5_answer', component_property='children'),
    [Input(component_id='q5_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div6(input_value1, input_value2, input_value3):
    q_index = 6
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q6_answer', component_property='children'),
    [Input(component_id='q6_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div7(input_value1, input_value2, input_value3):
    q_index = 7
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q7_answer', component_property='children'),
    [Input(component_id='q7_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div8(input_value1, input_value2, input_value3):
    q_index = 8
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_q8_answer', component_property='children'),
    [Input(component_id='q8_answer', component_property='value'),
     Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value')]
)
def update_output_div9(input_value1, input_value2, input_value3):
    q_index = 9
    st_id, degree = input_value2, input_value3
    text = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=num)
    return dcc.Markdown(text)


# 计算得分
@app.callback(
    Output(component_id='st_q9_answer', component_property='children'),
    [Input(component_id='my-id', component_property='value'),
     Input(component_id='degree', component_property='value'),
     Input(component_id='q0_answer', component_property='value'),
     Input(component_id='q1_answer', component_property='value'),
     Input(component_id='q2_answer', component_property='value'),
     Input(component_id='q3_answer', component_property='value'),
     Input(component_id='q4_answer', component_property='value'),
     Input(component_id='q5_answer', component_property='value'),
     Input(component_id='q6_answer', component_property='value'),
     Input(component_id='q7_answer', component_property='value'),
     Input(component_id='q8_answer', component_property='value'),
     Input(component_id='q9_answer', component_property='value')]
)
def update_output_score(st_id, degree, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    text = '\n************\n'
    answer_list = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    fig, st_score, st_auc = pw.plot(st_id, degree, num, answer_list)
    text += '**该学生得分为：%s**' % st_score

    book_score = pw.score2grade(st_score)
    df1 = pw.near_book(book_score, 3)
    df2 = pw.near_book(min(12, book_score+1), 3)
    books = list(set(list(df1['title']) + list(df2['title'])))
    book_text = '**推荐阅读：**' + ', '.join(books)

    if st_auc < 0.3:
        tip_text = 'tip：该阶段掌握较差，建议进行低一个阶段的测试'
    elif st_auc > 0.75:
        tip_text = 'tip：该阶段掌握较好，建议进行高一个阶段的测试'
    else:
        tip_text = ''

    return dcc.Markdown(text), dcc.Graph(figure=fig), dcc.Markdown(book_text), dcc.Markdown(tip_text)


@app.callback(
    Output(component_id='st_reaction', component_property='children'),
    [Input(component_id='my-id', component_property='value'),
     Input(component_id='my-grade', component_property='value'),
     Input(component_id='degree', component_property='value'),
     Input(component_id='my-book', component_property='value'),
     Input(component_id='my-reaction', component_property='value')]
)
def update_output_div4(input_value1, input_value2, input_value3, input_value4, input_value5):
    st_id, grade, st_degree, book, reaction = input_value1, input_value2, input_value3, input_value4, input_value5
    conn, connect = pw.conn_()
    sql = '''select * from text_table where title = "%s"''' % book
    df = pd.read_sql(sql, conn, )

    text = ''
    if len(df['title']) > 0 and reaction != '':
        try:
            log = pw.log_line(st_id, grade, st_degree, book, reaction)
            pw.save_log(log, 'log.txt')
            text = '反馈成功'
        except TypeError:
            text = '请重新反馈'
    elif reaction != '':
        text = '该书不在数据库中，请重新输入'
    text += '\n*****************************\n'
    return dcc.Markdown(text)


@app.callback(
    Output(component_id='st_txt', component_property='children'),
    [Input(component_id='txt', component_property='value')]
)
def update_output_div3(input_text):
    vec = pw.create_char(input_text)
    # get_text_degree输入是2D的数组
    pred = pw.get_text_degree([vec])
    df = pw.near_book(pred[0])
    title = list(df['title'])
    text = '''
    >该文案对应阅读难度：%s  (共1-12级)
    ''' % str(int(pred[0])) + '\n推荐阅读：\n'
    text = text + '，'.join(list(df['title']))
    text += '\n*****************************\n'
    return dcc.Markdown(text)


if __name__ == '__main__':
    app.run_server(debug=True)

