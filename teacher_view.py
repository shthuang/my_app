import pandas as pd
import dash_html_components as html
from sqlalchemy import create_engine
import pymysql
import dash_core_components as dcc
from plotly.graph_objs import *
import prepare_web as pw

global D
D = {1: '整体感知', 2: '信息获取', 3: '实际运用', 4: '鉴赏评价', 5: '解释推断'}


# 输入老师的班级，返回班级的学生最新的测试数据，其中班号是字符串
def class_st_table(class_id):
    db_name = 'classification_read'
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="09164528"
    )
    cursor = conn.cursor()
    conn.autocommit(1)
    # 选择数据库
    conn.select_db(db_name)
    connect = create_engine('mysql+pymysql://root:09164528@localhost:3306/" + db_name + "?charset=utf8mb4')

    sql = '''
        select * from 
            (select st_log.*, row_number() over (partition by st_log.st_id order by st_log.time desc) as `rows` 
             from st_log) t
            where t.rows = 1 and t.class_id = '%s';
    ''' % class_id
    df = pd.read_sql(sql, conn, )

    return df


# 输入学生表格，返回雷达图list和阅读建议list
def return_fig_read_list(df):
    st_part_list, part_list = df['st_part'], df['question_part']
    st_score = df['st_score']
    fig_list, book_list = [], []
    for i in range(len(st_part_list)):
        st_part, part = eval(st_part_list[i]), eval(part_list[i])
        r, theta = [], []
        # print([st_part, part])
        for key in part:
            if part[key] != 0:
                theta.append(D[key])
                r.append(st_part[key])

        st_data = [Scatterpolar(r=r, theta=theta, fill='toself')]
        plot_layout = Layout(
            title=str(df.iloc[i]['st_id']) + '\t阅读诊断：',
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            # showlegend=True
        )

        fig = Figure(data=st_data, layout=plot_layout)
        fig_list.append(dcc.Graph(figure=fig))

        # 推荐书籍
        book_score = pw.score2grade(st_score[i])
        df1 = pw.near_book(book_score, 3)
        df2 = pw.near_book(min(12, book_score + 1), 3)
        books = list(set(list(df1['title']) + list(df2['title'])))
        book_list.append(', '.join(books))

    return fig_list, book_list


# 表格展示
def generate_table(df, max_rows=200):
    fig_list, book_list = return_fig_read_list(df)
    show_df = df[['st_id', 'class_id', 'st_degree', 'st_auc', 'st_score']]
    show_df.columns = ['学生学号', '班号', '学生阅读等级', '准确率', '阅读能力得分']
    show_df['推荐阅读'] = book_list
    # 要补充每个人的阅读建议和测试建议
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in show_df.columns])] +

        # Body
        [html.Tr([
            html.Td(show_df.iloc[i][col]) for col in show_df.columns
        ]) for i in range(min(len(show_df), max_rows))]
    ), fig_list


if __name__ == '__main__':
    data = class_st_table(class_id='008')
    return_fig_read_list(data)
    print(data.columns)
    print(len(data))
    print(generate_table(data))
