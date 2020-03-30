import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

# app = DjangoDash('SimpleExample')   # replaces dash.Dash

# app.layout = html.Div([
#     dcc.RadioItems(
#         id='dropdown-color',
#         options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
#         value='red'
#     ),
#     html.Div(id='output-color'),
#     dcc.RadioItems(
#         id='dropdown-size',
#         options=[{'label': i,
#                   'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
#         value='medium'
#     ),
#     html.Div(id='output-size')
#
# ])
#
# @app.callback(
#     dash.dependencies.Output('output-color', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value')])
# def callback_color(dropdown_value):
#     return "The selected color is %s." % dropdown_value
#
# @app.callback(
#     dash.dependencies.Output('output-size', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value'),
#      dash.dependencies.Input('dropdown-size', 'value')])
# def callback_size(dropdown_color, dropdown_size):
#     return "The chosen T-shirt is a %s %s one." %(dropdown_size,
#                                                   dropdown_color)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Square Root slider graph"),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor":"#1a2d46", "color":"#ffffff"}),
    dcc.Slider(
        id='slider-updatemode',
        marks = {i:'{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag'
    ),
    # html.Div(id='updatemode-output-container', style={'margin-top':20})
])
#
# @app.callback([
#     Output('slider-graph', 'figure'),
#     Output('updatemode-output-container', 'children')],
#     [Input('slider-updatemode', 'value')]
# )


@app.callback(
    Output('slider-graph', 'figure'),
    [Input('slider-updatemode', 'value')]
)
def disply_value(value):
    x=[]
    for i in range(value):
        x.append(i)
    y=[]
    for i in range(value):
        y.append(i*i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='manipulate-graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis = dict(range=[min(x),max(x)]),
        yaxis = dict(range=[min(y),max(y)]),
        font=dict(color='white')
    )
    # return {"data":graph, "layout":layout}, f'Value:{round(value, 1)} square:{value*value}'
    return {"data":graph, "layout":layout}