# imports
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

# get data from the csv into a dataframe
df = pd.read_csv("data\daily_sales_data_pink_morsels.csv")

# converting to datetime to get the year etc
df[' Date'] = pd.to_datetime(df[' Date'])

#make a diagram from the data
fig = px.line(df, x=" Date", y="Sales", color=' Region', title="Pink Morsel sales")

# colour scheme
colours = {
    'north' : "#821F6E",
    'east' : "#AD4498",
    'south' : "#A38AE8",
    'west' : "#50CECA",
}


app.layout = html.Div( 
    style={
        'backgroundColor' : "#F2D7EE",
    },
    
    children=[
    # title
    html.H1(
        children='Pink morsel sales (Task 3)',
        style={
            'textAlign': 'center',
            'color': "#942A7F",
            'bgcolor': "#942A7F",

        }
    ),

    # question subtitle
    html.Div(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?', 
        id='header',
        style={
            'textAlign': 'center',
            'color' : "#C682BB"
    }),

    # regions title
    html.H2(children='Regions', 
        style={
            'textAlign': 'center',
            'color' : "#942A7F"
    }),


    # radio buttons to filter the different regions
    dcc.RadioItems(
        id='radio',
        options=[{'value': 'All'}] + [{'value': i} for i in df[' Region'].unique()],
        value = 'All',
        inline = True,

        # styling
        labelStyle={
            'color' : "#C682BB",
        },
        style={
            'textAlign': 'center',
            'bgcolor': "#942A7F",
        }
    ),

    # graph
    dcc.Graph(
        id='graph',
        figure=fig,
        # styling
        style={
            'plot_bgcolor' : "#F2D7EE",
            'color': "#942A7F",
            'accentColor' : "#50CECA",
        }
    ),

    # slider to filter the year
    dcc.Slider(
            df[' Date'].dt.year.min(),
            df[' Date'].dt.year.max(),
            step=1,
            marks= {str(year): str(year) for year in df[' Date'].dt.year.unique()},
            value=df[' Date'].dt.year.min(),
            id='slider',
        ),

])


# updates the graph when input changed
@callback(
Output('graph', 'figure'),
[Input('slider', 'value'), Input('radio', 'value')])
def update_figure(selected_year, selected_Region):

    # filters based off of selections
    filtered_df = df[df[' Date'].dt.year == selected_year]
    if selected_Region != 'All':
        filtered_df = filtered_df[filtered_df[' Region']==selected_Region]

    # re-renders
    fig = px.line(filtered_df, x=" Date", y="Sales", color=" Region", color_discrete_map=colours)

    fig.update_layout(
    template=None,
    plot_bgcolor="#FFF7FE",
    paper_bgcolor="#FFEBFC",
    font_color="#942A7F"
    )

    fig.update_layout()

    return fig


if __name__ == '__main__':
    app.run(debug=True)