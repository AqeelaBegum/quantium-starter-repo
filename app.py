# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# get data from the csv into a dataframe
df = pd.read_csv("data\daily_sales_data_pink_morsels.csv")

#make a diagram from the data
fig = px.line(df, x=" Date", y="Sales", color=' Region', title="Pink Morsel sales")

fig.update_layout(
    plot_bgcolor="#F2D7EE",
    paper_bgcolor="#FFF8FE",
    font_color="#942A7F"
)

# title
app.layout = html.Div( children=[
    html.H1(
        children='Pink morsel sales (Task 3)',
        style={
            'textAlign': 'center',
            'color': "#942A7F"

        }
    ),

    # question subtitle
    html.Div(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?', 
        style={
            'textAlign': 'center',
            'color' : "#C682BB"
    }),

    dcc.Graph(
        id='graph',
        figure=fig,
    )
])


if __name__ == '__main__':
    app.run(debug=True)