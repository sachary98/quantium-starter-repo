from dash.testing.composite import DashComposite
from dash.testing.application_runners import import_app
import pytest

app = import_app('hash_demo')

@pytest.fixture
def dash_duo():
    return DashComposite(app)

def test_header_present(dash_duo):
    dash_duo.start_server()
    header = dash_duo.find_element("#header")
    assert header.text == "Hello Dash"

def test_visualization_present(dash_duo):
    dash_duo.start_server()
    graph = dash_duo.find_element("#region-graph")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server()
    region_picker = dash_duo.find_element("#region")
    assert region_picker is not None
    