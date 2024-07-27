# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv(r'.\final_file.csv')

plot_1 = px.line(data, x='date', y='sales')

app.layout = html.Div(children = [
    html.H1(children = 'Sales of Soul\'s Food (Pink Morsel)',
            style  = {'textAlign' : 'center'}),
    dcc.Graph(
        id = 'Line-Chart',
        figure = plot_1
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
