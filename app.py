# app.py

import dash
from layout import app_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the app layout
app.layout = app_layout

# Register the callbacks
register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
