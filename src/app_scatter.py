import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/gdp-life-exp-2007.csv')

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                size='population', color='continent', hover_name="country",
                log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__=='__main__':
    app.run_server(debug=True)