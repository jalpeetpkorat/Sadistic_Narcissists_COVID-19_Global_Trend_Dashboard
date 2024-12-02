# layout.py

import dash_core_components as dcc
import dash_html_components as html
from data import load_data

# Load data from the data module
country_data, confirmed_data, deaths_data, vaccination_data = load_data()

# Define the layout of the app
app_layout = html.Div(
    style={"font-family": "Arial, sans-serif", "background-color": "#f7f8fc", "padding": "20px"},
    children=[
        html.Div(
            children=[
                html.H1(
                    "COVID-19 Global Trend Dashboard",
                    style={
                        "textAlign": "center",
                        "color": "#2c3e50",
                        "font-size": "40px",
                        "font-weight": "bold",
                        "padding-bottom": "20px",
                        "margin-top": "0px"
                    }
                ),
                html.P(
                    "Explore the global trend of COVID-19 cases, deaths, and vaccinations in real time. Get insights on the impact of the pandemic worldwide.",
                    style={
                        "textAlign": "center",
                        "font-size": "18px",
                        "color": "#7f8c8d",
                        "margin-bottom": "30px",
                        "max-width": "800px",
                        "margin": "0 auto"
                    }
                ),
            ]
        ),
        
        # Country selection dropdown
        html.Div(
            children=[
                dcc.Dropdown(
                    id="country-dropdown",
                    options=[{"label": country, "value": country} for country in country_data["Country"].unique()],
                    value="India",
                    style={
                        "width": "80%",
                        "margin": "auto",
                        "font-size": "18px",
                        "margin-bottom": "30px",
                        "background-color": "#ecf0f1",
                        "border-radius": "8px",
                        "padding": "12px",
                        "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    }
                )
            ]
        ),
        
        # Data type selection dropdown
        html.Div(
            children=[
                dcc.Dropdown(
                    id="data-dropdown",
                    options=[
                        {"label": "Confirmed Cases", "value": "Confirmed Cases"},
                        {"label": "Deaths", "value": "Deaths"},
                        {"label": "Vaccinations", "value": "Vaccinations"}
                    ],
                    value="Confirmed Cases",
                    style={
                        "width": "80%",
                        "margin": "auto",
                        "font-size": "18px",
                        "margin-bottom": "30px",
                        "background-color": "#ecf0f1",
                        "border-radius": "8px",
                        "padding": "12px",
                        "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    }
                )
            ]
        ),
        
        # Map visualization for COVID-19 data
        html.Div(
            children=[
                dcc.Graph(
                    id="map-graph",
                    config={"scrollZoom": True, "displayModeBar": True},
                    style={"height": "500px", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "border-radius": "10px"}
                )
            ]
        ),
        
        # Time-series graph for selected country
        html.Div(
            children=[
                dcc.Graph(
                    id="time-series-graph",
                    style={"height": "500px", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "border-radius": "10px"}
                )
            ]
        ),
    ]
)
