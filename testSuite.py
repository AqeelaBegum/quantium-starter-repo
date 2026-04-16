# imports
from dash import Dash, dcc, html, Input, Output, callback
import dash
from dash import html
import plotly.express as px
import pandas as pd

from app import app, update_figure

# header test
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#header', timeout=5)
    assert dash_duo.get_logs() == [], "header present, no error"

# region picker test
def test_region_picker_present(dash_duo):
    dash_duo.start_server()
    dash_duo.wait_for_element('#radio', timeout=5)
    assert dash_duo.get_logs() == [], "region picker present"

# graph test
def test_graph_present(dash_duo):
    dash_duo.start_server()
    dash_duo.wait_for_element('#graph')
    assert dash_duo.get_logs() == [], "graph/visualiser present"
