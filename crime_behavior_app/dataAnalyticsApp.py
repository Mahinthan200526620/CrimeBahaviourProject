import dash
from dash import html
from dash.dependencies import Output, Input
from dash import dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# read in data
data = pd.read_csv("assets/clean_crime_canada_dataset.csv")
data["year"] = data["year"].astype(int)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Group 4 - Data Analytics Project"

app.layout = dbc.Container(
    html.Div([
        html.Hr(),
        dbc.Row([
            dbc.Col(
                [
                    html.Label("Years"),
                    dcc.Dropdown(
                        id="year-selector",
                        options=[{"label": year, "value": year} for year in data["year"].unique()],
                        value=data["year"].max(),
                        clearable=False
                    ),
                ],
                md=3,
            ),
            dbc.Col(
                [
                    html.Label("Locations"),
                    dcc.Dropdown(
                        id="location-selector",
                        options=[{"label": location, "value": location} for location in data["location"].unique()],
                        placeholder="Select a location",
                    ),
                ],
                md=3,
            ),
            dbc.Col(
                html.Div([
                    html.H4("Total Crimes", className="card-title"),
                    html.P(id="incidents-total"),
                ])
            ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(dcc.Graph(
                id="graphs-by-selection",
            ), md=12),
        ]),
        # html.Hr(),
        # dbc.Row([
        #     dbc.Col(dcc.Graph(id="incidents-by-type-graph"), md=12),
        # ])
    ])
)

# Define the second callback
@app.callback(
    [
        Output("incidents-total", "children"),
        Output("graphs-by-selection", "figure")
        # Output("incidents-by-region-graph", "figure"),
        # Output("incidents-by-type-graph", "figure")
    ],
    [
        Input("year-selector", "value"),
        Input("location-selector", "value"),
    ]
)
def update_graphs(selected_year: int, selected_location: str):
    incidents_total = data[data["year"] == selected_year]["incidents"].sum(numeric_only=True)
    if isinstance(selected_year, int) and selected_year is not None and selected_year >= 0:
        if selected_location is not None and len(selected_location) > 0:
            filtered_df = data.loc[(data["year"] == selected_year) & (data["location"] == selected_location)]
            # incidents_by_location = filtered_df.groupby("location").sum(numeric_only=True)["incidents"]
            incidents_by_crime_type = filtered_df.groupby("type_of_crime").sum(numeric_only=True)["incidents"]
            fig = px.bar(
                incidents_by_crime_type,
                title=f"Number of Crimes by Type in {selected_year} in {selected_location}",
                x=incidents_by_crime_type.index,
                y='incidents',
                labels={
                    'type_of_crime': 'Type of Crimes',
                    'incidents': 'No. of Crimes'
                },
            )
            # fig = px.bar(
            #     incidents_by_location,
            #     title=f"Number of Crimes by Location in {selected_year}",
            #     x=incidents_by_location.index,
            #     y='incidents',
            #     labels={
            #         'location': 'Location',
            #         'incidents': 'No. of Crimes'
            #     },
            # )
        else:
            # filtered_df = data.loc[data["year"] == selected_year]
            incidents_by_year = data.groupby("year").sum(numeric_only=True)["incidents"]
            fig = px.line(
                incidents_by_year,
                title=f"Number of all types of crimes by Year in all the locations",
                x=incidents_by_year.index,
                y='incidents',
                labels={
                    'year': 'Years',
                    'incidents': 'No. of Crimes'
                },
            )

    return incidents_total, fig


if __name__ == "__main__":
    app.run_server(debug=True)
