from dash import Dash
from visualization import layout
from callbacks import register_callbacks

# Initialize Dash app
app = Dash(__name__)
app.layout = layout()

# Register callbacks
register_callbacks(app)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
