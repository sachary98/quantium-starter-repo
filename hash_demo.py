from dash import html,dash,dcc,Input,Output,callback
import pandas as pd
import plotly.express as px
import numpy as np

app = dash.Dash(__name__)

file = pd.read_csv(r'.\final_file.csv')

app.layout = html.Div([
    html.Div([
        html.Label('Select Region'),
        dcc.RadioItems(np.append(file["region"].unique(),'all'), 'north', id='region')
    ],style={
        'width':'10%',
        'border':'2px solid black',
        'border-radius':'15px',
        'padding':'20px',
    }
    ),
    dcc.Graph(id='region-graph')
], style={'background-color':'#2560CF'}
)

@callback(
    Output('region-graph', 'figure'),
    Input('region', 'value')
)
def update_graph(region):
    if region == 'all':
        df = file
    else:    
        df = file[file['region'] == region]
        
    fig = px.line(df, x='date',y='sales')
    fig.update_traces(line=dict(color='#5BB6FF'))
    
    fig.update_layout(
    plot_bgcolor='#2560CF', 
    paper_bgcolor='#2560CF',
    xaxis=dict(
        showgrid=False,
    ),
    yaxis=dict(
        gridcolor='black',
        gridwidth=2
    )
    )   
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)