from flask import Flask
from config import Config

# Flask constructor takes the name of
# current module (__name__) as argument.
def create_app(config_class=Config):
    app = Flask(__name__)
    # attach configuration here
    app.config.from_object(config_class)
    # attach extensions and blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # attach routes and custom error pages here
    return app