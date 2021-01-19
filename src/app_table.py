import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('./data/usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children="US Agriculture Reports (2011)"),
    generate_table(df)
])

if __name__=='__main__':
    app.run_server(debug=True)