# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:44:06 2019

@author: 17968
"""
# -*- coding: utf-8 -*-

import dash
import dash_core_components
import dash_html_components

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output 
import plotly.graph_objs as go

home = '结果/'

import plot_map as pm
import plot_wordcloud as pw
import select_data as sd
import plot_main2 as plot2


app = dash.Dash()


def plot_bar(app, x, y, name):
    
    app.layout = dash_html_components.Div(children=[
        dash_html_components.H1(children='Testme'),
        dash_core_components.Graph(
        id='bar',#修改图像类型
        figure={
        'data': [
        {'x': x, 'y': y, 'type': 'bar', 'name': name},
        ],
        'layout': {
        'title': 'Test Curve'
        } } )
    ])

    
def option_list(mode='city'):
    
    op_list = []
    if(mode=='province'):
        province_list = sd.get_province()
        for line in province_list['province']:
            #l = line
            op_list.append({'label':line, 'value':line})
    else:
        city_list = sd.get_city()
        for line in city_list['city']:
            #l = line
            op_list.append({'label':line, 'value':line})  
    
    return op_list
            
        

def choose(op_list, mode='city'):
 
    app = dash.Dash()
    
    if(mode == 'city'):
        app.layout = html.Div([
            html.Label('请选择城市：'),
            dcc.Dropdown(
                id = 'city',
                options = op_list,
                value = '广州'
                #multi=True
            ),
    
        html.Div(id = 'city_bar')
        ], style={'columnCount': 1})
    elif(mode == 'province'):
        app.layout = html.Div([
            html.Label('请选择省份：'),
            dcc.Dropdown(
                id = 'city',
                options = op_list,
                value = '广东'
                #multi=True
            ),
    
        html.Div(id = 'city_bar')
        ], style={'columnCount': 1})   

    @app.callback(
        Output(component_id = 'city_bar', component_property = 'children'),
        [Input(component_id = 'city', component_property = 'value')]
    )
    def update_graph(value):
        print(value)
        
        if(mode=='city'):
            data_x, data_y = plot2.get_mons_city(value)
        else:
            data_x, data_y = plot2.get_mons_province(value)
        #print(data_y[0])
        
        trace = go.Bar(
                x = data_x,
                y = data_y,
                name = value,
                hoverlabel={ #设置浮标的样式
                        #浮标背景颜色，可以是一个颜色，也可以是每个柱子都不一样 
                        'bgcolor': 'white',            
                        'bordercolor': '#000000', #浮标外框颜色
                         },
                marker = {
                        'color':['salmon', 'sandybrown', 'orange', 'khaki', 
                                 'greenyellow', 'green', 'skyblue', 
                                 'slateblue', 'darkorchid', 'plum', 
                                 'purple', 'pink'],
                        }
                )
        
        layout = go.Layout(
                title = value + '每月总评论数目柱状图',
                xaxis = {'title':'月份'},
                yaxis = {'title':'评论数目'}
                )
        
        return html.Div([
                html.H3('对应柱状图：'),
                dcc.Graph(
                    id = 'city_bar' + value,
                    figure = go.Figure(
                            data = trace,
                            layout = layout
                            ) 
                    )
                ])
    
    app.run_server(debug=False)


if __name__ == '__main__':
    
    print('\nRunning on http://127.0.0.1:8050/ (Press CTRL+C to quit)\n\n')
    #plot_bar(app, x, y)
    
    op_list = option_list(mode='city')
    choose(op_list, mode='city')
    
    '''
    op_list2 = option_list(mode='province')
    choose(op_list2, mode='province')
    '''

















