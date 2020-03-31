import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from plotly.offline import iplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dashboard_app.views import *


app = DjangoDash('SimpleExample')

app.layout = html.Div([
    html.H1("Student marks graph"),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor":"#1a2d46", "color":"#ffffff"}),
    dcc.Markdown('''

    ''',
    id='slider-updatemode'),

    html.Div(id='updatemode-output-container', style={'margin-top':20})
])

@app.callback(
    Output('slider-graph', 'figure'),
    [Input('slider-updatemode', 'id')]
)
def disply_value(value):
    output = testing()
    # working_dir = os.getcwd()
    # file_loc = working_dir + '/dashboard_app/dash_apps/student_marks.csv'
    # timesData = pd.read_csv(file_loc)
    # df = timesData.iloc[:100, :]
    # trace2 = go.Scatter(
    #     x=df.Biology,
    #     y=df.English,
    #     mode="lines+markers",
    #     name="Marks",
    #     marker=dict(color='rgba(80, 26, 80, 0.8)'),
    #     text=df.Name)
    # data = [trace2]
    # layout = dict(title='Student Marks',
    #               xaxis=dict(title='Biology', ticklen=5, zeroline=False),
    #               yaxis= dict(title='English', ticklen=5, zeroline=False),
    #               hovermode='closest'
    #               )
    # return {"data": data, "layout": layout}
    return output
