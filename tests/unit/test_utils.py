"""
This file (test_app.py) contains the unit tests for the Flask application.
"""
import pytest
from pydantic import ValidationError
from utils.berry_stats import BerryStats

@pytest.mark.skip(reason="TODO for next iteration")
def test_validate_berrystats_fetch():
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    pass

@pytest.mark.skip(reason="TODO for next iteration")
def test_validate_berrystats_calculate():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (invalid rating) is passed in
    THEN check that the validation raises a ValueError
    """
    pass

@pytest.mark.skip(reason="TODO for next iteration")
def test_validate_berrystats_histogram():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (invalid title) is passed in
    THEN check that the validation raises a ValidationError
    """
    pass
