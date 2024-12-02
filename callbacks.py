# callbacks.py

import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
from data import load_data

# Load data
country_data, confirmed_data, deaths_data, vaccination_data = load_data()

# Define the callbacks for updating the map and time-series graph
def register_callbacks(app):

    @app.callback(
        [Output("map-graph", "figure"),
         Output("time-series-graph", "figure")],
        [Input("country-dropdown", "value"),
         Input("data-dropdown", "value")]
    )
    def update_map_and_graph(selected_country, selected_data):
        if selected_data == "Confirmed Cases":
            color_column = "Confirmed Cases"
            title_map = f"COVID-19 Confirmed Cases in {selected_country}"
            title_graph = f"COVID-19 Confirmed Cases Over Time for {selected_country}"
        elif selected_data == "Deaths":
            color_column = "Deaths"
            title_map = f"COVID-19 Deaths in {selected_country}"
            title_graph = f"COVID-19 Deaths Over Time for {selected_country}"
        else:
            color_column = "Vaccinations"
            title_map = f"COVID-19 Vaccinations in {selected_country}"
            title_graph = f"COVID-19 Vaccinations Over Time for {selected_country}"

        selected_data_df = country_data[country_data["Country"] == selected_country]
        
        # Map Plotly
        map_fig = go.Figure(
            data=go.Choropleth(
                locations=selected_data_df["Country"],
                z=selected_data_df[color_column],
                hoverinfo="location+z",
                colorscale="Viridis"
            )
        )
        map_fig.update_layout(title=title_map, geo=dict(showcoastlines=True))
        
        # Time-series Plotly
        if selected_data == "Confirmed Cases":
            data_df = confirmed_data[confirmed_data["Country"] == selected_country]
        elif selected_data == "Deaths":
            data_df = deaths_data[deaths_data["Country"] == selected_country]
        else:
            data_df = vaccination_data[vaccination_data["location"] == selected_country]
        
        time_series_fig = px.line(
            data_df,
            x="Date",
            y=color_column,
            title=title_graph
        )
        time_series_fig.update_layout(
            xaxis_title="Date",
            yaxis_title=selected_data,
            showlegend=False
        )
        
        return map_fig, time_series_fig
