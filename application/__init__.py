from flask import Flask, g
import logging

# Global variables


def create_app():
    """Initialize core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    logging.basicConfig(level=logging.DEBUG)
    logging.disable(logging.DEBUG)
    # Initialize Plugins

    with app.app_context():
        from application import routes

        # Register Blueprints

        return app
