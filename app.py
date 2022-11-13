# Run this app with `python app.py`

from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

app = Dash(__name__)

server = app.server

tips = pd.read_csv('RestaurantTips.csv')

def make_correlation_heatmap():
    tips_cor = tips.corr()

    fig = px.imshow(
    tips_cor, 
    text_auto=True, 
    aspect="auto", 
    )
    
    fig.update_traces(texttemplate="%{z:.2f}")

    return fig

def make_scatter_plot():
    fig = px.scatter(
        tips, 
        x="total_bill", 
        y="tip", 
        color="sex",
        size = "size", 
        symbol="smoker", 
        facet_col="day",
        facet_row = "time", 
        labels={"sex": "Gender", "smoker": "Smokes"},
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
        "time": ["Lunch", "Dinner"]})

    fig.update_xaxes(title_text = "Total Bill ($)")
    fig.update_yaxes(title_text = "Tips ($)")

    return fig

app.layout = html.Div(children=[
    html.H1(children = "Restaurant Tips Exploratory Data Analysis", style={
        "textAlign": "center",
        "font-size": "70px",
        "font-weight": "600",
        "background-image": "linear-gradient(to right, #553c9a 45%, #ee4b2b)",
        "color": "transparent",
        "background-clip": "text",
        "-webkit-background-clip": "text",
}),
    html.Div(children='''
         This data set is from our local restaurant.
    '''),
    html.H2(children='Correlation Heatmap', style={
        "font-size": "45px",
        "font-weight": "400",
        "background-image": "linear-gradient(to right, #553c9a 45%, #ee4b2b)",
        "color": "transparent",
        "background-clip": "text",
        "-webkit-background-clip": "text",
    }),
    dcc.Graph(
        id='correlation_graph',
        figure=make_correlation_heatmap()
        ),
        
        
    html.H2(children='Scatter comparing Total Bill and Tips', style={
        "font-size": "45px",
        "font-weight": "400",
        "background-image": "linear-gradient(to right, #553c9a 45%, #ee4b2b)",
        "color": "transparent",
        "background-clip": "text",
        "-webkit-background-clip": "text",
    }),
    dcc.Graph(id='scatter_graph',
        figure=make_scatter_plot()
    ),
])

# Start the server
if __name__ == '__main__':
    app.run_server(debug=True)
