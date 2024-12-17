from dash import html, dcc
from data_processing import get_country_summary, load_data

# Load data
confirmed_data, deaths_data, vaccination_data = load_data()
country_data = get_country_summary(confirmed_data, deaths_data, vaccination_data)

def layout():
    return html.Div(
        style={
            "font-family": "Arial, sans-serif",
            "background-color": "#F7F9FC",
            "padding": "20px",
            "border-radius": "10px",
            "box-shadow": "0 4px 8px rgba(0,0,0,0.2)",
            "max-width": "1200px",
            "margin": "auto"
        },
        children=[
            html.H1(
                "🌍 COVID-19 Global Dashboard 🌍",
                style={"textAlign": "center", "color": "#2c3e50"}
            ),
            html.Div(
                style={"display": "flex", "justify-content": "center", "gap": "20px"},
                children=[
                    # Country Dropdown populated dynamically
                    dcc.Dropdown(
                        id="country-dropdown",
                        options=[
                            {"label": country, "value": country}
                            for country in country_data["Country"].unique()
                        ],
                        value="India",  # Default value
                        placeholder="Select a Country",
                        style={
                            "width": "40%",
                            "font-size": "16px",
                            "background-color": "#ffffff",
                            "border-radius": "8px",
                            "box-shadow": "0 2px 4px rgba(0,0,0,0.1)"
                        }
                    ),
                    dcc.Dropdown(
                        id="data-dropdown",
                        options=[
                            {"label": "Confirmed Cases", "value": "Confirmed Cases"},
                            {"label": "Deaths", "value": "Deaths"},
                            {"label": "Vaccinations", "value": "total_vaccinations"}
                        ],
                        value="Confirmed Cases",
                        placeholder="Select Data Type",
                        style={
                            "width": "40%",
                            "font-size": "16px",
                            "background-color": "#ffffff",
                            "border-radius": "8px",
                            "box-shadow": "0 2px 4px rgba(0,0,0,0.1)"
                        }
                    ),
                ]
            ),
            dcc.Graph(id="map-graph", config={"scrollZoom": False}),
            dcc.Graph(id="time-series-graph")
        ]
    )
