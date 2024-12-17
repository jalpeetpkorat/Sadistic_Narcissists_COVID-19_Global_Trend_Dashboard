import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
from data_processing import load_data, get_country_summary

# Load data
confirmed_data, deaths_data, vaccination_data = load_data()
country_data = get_country_summary(confirmed_data, deaths_data, vaccination_data)

def register_callbacks(app):
    @app.callback(
        [Output("map-graph", "figure"), Output("time-series-graph", "figure")],
        [Input("country-dropdown", "value"), Input("data-dropdown", "value")]
    )
    def update_visualizations(selected_country, selected_data):
        # Choropleth map
        map_figure = go.Figure(go.Choropleth(
            locations=country_data["Country"],
            locationmode="country names",
            z=country_data[selected_data],
            colorscale="Blues",
            colorbar_title=selected_data
        ))
        map_figure.update_layout(title=f"Global {selected_data} Data")

        # Time-series graph
        if selected_data == "total_vaccinations":
            ts_data = vaccination_data[vaccination_data["Country"] == selected_country]
        elif selected_data == "Confirmed Cases":
            ts_data = confirmed_data[confirmed_data["Country/Region"] == selected_country]
        else:
            ts_data = deaths_data[deaths_data["Country/Region"] == selected_country]

        if ts_data.empty:
            time_series_figure = go.Figure()
            time_series_figure.update_layout(title=f"No {selected_data} Data Available")
        else:
            time_series_figure = px.line(
                ts_data, x="Date", y=selected_data,
                title=f"{selected_data} Over Time in {selected_country}"
            )
        return map_figure, time_series_figure
