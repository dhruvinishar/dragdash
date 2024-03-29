# Author: Dhruvi Nishar
# Date: 17/03/23
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All the imports
#import dash, plotly, and dash for jupyter notebook 
from dash import dash, html
import plotly.express as px
import plotly.graph_objs as go
from jupyter_dash import JupyterDash #for jupyter notebook

#import front end libraries 
import dash_core_components as dcc #core components for front end 
import dash_html_components as html #html components for front end
import dash_bootstrap_components as dbc #boostrap components for front end
from dash.dependencies import Input, Output

#other packages 
import pandas as pd
import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Read the data
# Data from https://cran.r-project.org/web/packages/dragracer/index.html
rpdr_c = pd.read_csv('data/rpdr_contestants.csv')
rpdr_cp = pd.read_csv('data/rpdr_contestant_performance.csv')
rpdr_e = pd.read_csv('data/rpdr_episodes.csv')
df = pd.read_csv('data/drag.csv')

# Data Cleaning and Pre-processing before visualizing
# Remove episodes where no ranked competition occurred (i.e. the reunion)
to_remove = rpdr_cp[(rpdr_cp['episode'] == 13) & (rpdr_cp['season'].isin(['S11', 'S12']))]
rpdr_cp = rpdr_cp.drop(to_remove.index)

# Regroup episode rankings
# Making it to the finale is considered a win, OUT = not in episode/or eliminated both included
outcome_map = {'OUT': 'OUT', 'LOST1ST ROUND': 'OUT', 'LOST2ND ROUND': 'OUT', 'LOST3RD ROUND': 'OUT', 'MISSCON': 'OUT',
               'DISQ': 'OUT', 'RTRN': 'OUT', 'SAFE+DEPT': 'OUT', 'BTM': 'BOTTOM', 'TOP2': 'WIN', 'WIN+RTRN': 'WIN'}
rpdr_cp['outcome2'] = rpdr_cp['outcome'].replace(outcome_map)

#filter to winners only 
winners = rpdr_cp[rpdr_cp['rank'] == 1]
#remove index 1706, 676 for seasons where winner did not compete in first episode
winners.drop([676, 1706], axis = 0, inplace = True)

#scale outcomes 
winners['outcome_count'] = winners.groupby('contestant')['participant'].transform('count')
winners['outcome_count_scaled'] = winners['outcome_count']/winners.groupby('contestant')['outcome_count'].transform('sum')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Img(src='assets/logo.png', height='80px', style={'float': 'left'}),
    html.H6(
        children = 'Queen Performance by Season',
        style = {'textAlign': 'left-center', 
                 'color': '#FF1D8E',
                 'font-family': 'Brush Script MT',
                 'font-size': '55px'}),
    dcc.Dropdown(
        id = 'season_dropdown', clearable = False,
        value = 'S07',
        options = [{'label':i, 'value': i} for i in rpdr_cp['season'].unique()],
        style = {'width': '75%', 
                 'margin': 'auto'}
    ),
    dcc.Graph(
        id='rpdr_graph',
        figure= {}
    ),
    html.H6(
        children = 'Winner Performance in Retrospect',
        style = {'textAlign': 'center', 
                 'color': '#FF1D8E',
                 'font-family': 'Brush Script MT',
                 'font-size': '55px'}),
    dcc.Graph(
        id='winners_graph',
        figure= {}
    )
]
)

@app.callback( 
    [Output('rpdr_graph', 'figure'), Output('winners_graph', 'figure')], 
    [Input('season_dropdown', 'value')]) 
def update_graph(season):
    s_x = rpdr_cp[rpdr_cp['season'] == str(season)]
    fig1 = px.bar(s_x, x='contestant', color = 'outcome2', 
                 labels={'count':'Total performance', 
                         'contestant':'Queens (by Rank)',
                         'outcome2':'Outcome'},
                 color_discrete_sequence=['#636EFA', '#FF6692', '#00CC96', '#FFA15A', '#FFFF7C','#999999'],
                 category_orders={"outcome2": ["WIN", "HIGH", "SAFE", "LOW", "BOTTOM","OUT"]})

    fig1.update_layout(legend_traceorder='normal',
                       xaxis={'categoryorder':'array', 
                            'categoryarray':s_x['contestant'].unique()},
                 plot_bgcolor='#F7DAE4')
    
    fig1.update_traces(marker=dict(line=dict(width=0.7, color='black')))

    fig2 = px.bar(winners, x = 'contestant', y = 'outcome_count_scaled', color = 'outcome2',
            labels={'outcome_count_scaled':'Relative Performance', 
                    'contestant':'Winner (in order of season)',
                    'outcome2':'Outcome'},
                 color_discrete_sequence=['#636EFA', '#FF6692', '#00CC96', '#FFA15A', '#FFFF7C', '#999999'],
                 category_orders={"outcome2": ["WIN", "HIGH", "SAFE", "LOW", "BOTTOM", "OUT"]})

    fig2.update_layout(legend_traceorder='normal',
                       plot_bgcolor='#F7DAE4')
    
    fig2.update_traces(marker=dict(line=dict(width=0.7, color='black')))

    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True, port=3333)