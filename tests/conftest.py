import os
import pytest
from app import create_app
from config import Config

# --------
# Config
# --------

class TestConfig(Config):
    TESTING = True

# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration for creating the Flask application
    flask_app = create_app(TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client
