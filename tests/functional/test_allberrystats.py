"""
This file (test_allberrystats.py) contains the functional tests for the pokeapi endpoints.

These tests use GETs and POSTs to different URLs to check for the proper behavior.
"""
import json
from app import create_app

def test_home_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert "Hello World" in response.data.decode('utf-8')

def test_home_page_post_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405

def test_get_endpoint_not_found(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that a '404' (Not Found) status code is returned
    """
    response = test_client.get('/non_existent_endpoint')
    assert response.status_code == 404

def test_allberrystats_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/allBerryStats' page is posted to (GET)
    THEN check that the response is valid and all required JSON fields are present in the response
    """
    response = test_client.get('/allBerryStats')

    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'berries_names' in data
    assert 'min_growth_time' in data
    assert 'median_growth_time' in data
    assert 'max_growth_time' in data
    assert 'variance_growth_time' in data
    assert 'mean_growth_time' in data
    assert 'frequency_growth_time' in data

def test_allberrystats_page_with_monkeypatch_error_fixture(patched_test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/allBerryStats' page is posted to (GET) but the ARG_POKEAPI_BERRY_BASE_URL is set to a wrong value
    THEN check that the response is invalid (500)
    """
    response = patched_test_client.get('/allBerryStats')
    assert response.status_code == 500