# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
from utils.berry_stats import BerryStats
import os
from app.main import bp

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@bp.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@bp.route('/allBerryStats')
def all_berry_stats():
    url = os.getenv('POKEAPI_BERRY_BASE_URL')
    print(url)
    allBerryStats = BerryStats(url)
    allBerryStats.fetch_stats()
    stats_dict = allBerryStats.calculate_stats()
    print(stats_dict)
    return jsonify(stats_dict)