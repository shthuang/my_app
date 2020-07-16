import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import prepare_web as pw
from get_test_score import load_exam_paper


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

q_index = 2
st_id, degree = 1966, 2
text1 = pw.str_text_question(q_index=q_index, st_id=st_id, degree=degree, num=17)
print(text1)
df = load_exam_paper(8, 1, int(st_id)).reset_index()
text2 = df['question'][0]
print(text2)

app.layout = html.Div([
    dcc.Markdown(children=text1),
    dcc.Markdown(children=text2)]
)

app.run_server(debug=True)
