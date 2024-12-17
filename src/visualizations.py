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
            html.P(
                "Visualize the global trends in COVID-19 confirmed cases, deaths, and vaccinations.",
                style={"textAlign": "center", "color": "#555", "fontSize": "16px"}
            ),
            # Centered Dropdown Container
            html.Div(
                style={
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "margin-bottom": "30px",
                    "gap": "50px",  # Controls horizontal spacing
                },
                children=[
                    html.Div(
                        style={"width": "40%"},
                        children=dcc.Dropdown(
                            id="country-dropdown",
                            options=[
                                {"label": country, "value": country}
                                for country in country_data["Country"].unique()
                            ],
                            value="India",
                            placeholder="Select a Country",
                        )
                    ),
                    html.Div(
                        style={"width": "40%"},
                        children=dcc.Dropdown(
                            id="data-dropdown",
                            options=[
                                {"label": "Confirmed Cases", "value": "Confirmed Cases"},
                                {"label": "Deaths", "value": "Deaths"},
                                {"label": "Vaccinations", "value": "People Vaccinated"}
                            ],
                            value="Confirmed Cases",
                            placeholder="Select Data Type",
                        )
                    ),
                ]
            ),
            # Graphs Section
            dcc.Graph(id="map-graph", config={"scrollZoom": False}),
            dcc.Graph(id="time-series-graph")
        ]
    )
