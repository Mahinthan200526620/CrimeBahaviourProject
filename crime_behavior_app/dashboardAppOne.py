# import dash
# from dash import html
# from dash.dependencies import Output, Input
# from dash import dcc
# import plotly.express as px
# import pandas as pd
# import dash_bootstrap_components as dbc
#
# # read in data
# # data = pd.read_csv("assets/precious_metal_prices.csv")
# data = pd.read_csv("assets/clean_crime_canada_dataset.csv")
# # # create a plotly figure for use by dcc.Graph()
# # fig = px.line(
# #     data,
# #     title="Metal prices by date",
# #     x="Date",
# #     y=["Gold AM Fix"],
# #     color_discrete_map={"Gold AM Fix": "green"}
# # )
# fig1 = px.bar(
#     data,
#     title="Crimes Count by Location",
#     x="location",
#     y=["incidents"],
#     color_discrete_map={"incidents": "red"}
# )
# fig2 = px.bar(
#     data,
#     title="Crimes Count by Type",
#     x="type_of_crime",
#     y=["incidents"],
#     color_discrete_map={"incidents": "blue"}
# )
# app = dash.Dash(__name__)  # external_stylesheets=[dbc.themes.BOOTSTRAP]
# app.title = "Group 4"
#
# app.layout = html.Div(
#     id="app-container",
#     children=[
#         # html.Div(
#         #     id="header-area",
#         #     children=[
#         #         html.H1(
#         #             id="header-title",
#         #             children="Precious Metal Prices"
#         #         ),
#         #         html.P(
#         #             id="header-description",
#         #             children=("The cost of metal ", html.Br(), "by the date")
#         #         )
#         #     ]
#         # ),
#         # html.Hr(),
#         # html.Div(
#         #     id="menu-area",
#         #     children=[
#         #         html.Div(
#         #             children=[
#         #                 html.Div(
#         #                     children="Metals"
#         #                 ),
#         #                 dcc.Dropdown(
#         #                     id="metal-filter",
#         #                     options=[{"label": metal, "value": metal} for metal in data.columns[1:]],
#         #                     clearable=False,
#         #                     value="Gold AM Fix"
#         #                 )
#         #             ],
#         #         ),
#         #     ]
#         # ),
#         html.Hr(),
#         html.Div(
#             id="graph-container1",
#             children=[
#                 dcc.Graph(
#                     id="crime-data-chart1",
#                     figure=fig1,
#                     config={"displayModeBar": False}
#                 )
#             ]
#         ),
#         html.Hr(),
#         html.Div(
#             id="graph-container1",
#             children=[
#                 dcc.Graph(
#                     id="crime-data-chart2",
#                     figure=fig2,
#                     config={"displayModeBar": False}
#                 )
#             ]
#         )
#     ]
# )
#
# # @app.callback(
# #     Output("price-chart", "figure"),
# #     Input("metal-filter", "value")
# # )
# # def update_chart(metal):
# #     fig = px.line(
# #         data,
# #         title="Metal prices by date",
# #         x="Date",
# #         y=[metal],
# #         color_discrete_map={
# #             "Gold AM Fix": "gold",
# #             "Gold PM Fix": "gold",
# #             "Silver Fix": "silver",
# #             "Platinum AM Fix": "#E5E4E2",
# #             "Platinum PM Fix": "#E5E4E2",
# #             "Palladium AM Fix": "#CED0DD",
# #             "Palladium PM Fix": "#E5E4E2"
# #         }
# #     )
# #
# #     fig.update_layout(
# #         template="plotly_dark",
# #         xaxis_title="Date",
# #         yaxis_title="Price(USD)",
# #         font=dict(
# #             family="Verdana, sans-serif",
# #             size=11,
# #             color="white"
# #         )
# #     )
# #     return fig
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
