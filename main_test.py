# main_test.py

import pytest
from main import app # Import the Flask app instance from your main.py

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the '/' endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps Students!" in response.data