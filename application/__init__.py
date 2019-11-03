from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


# Global variables
db = SQLAlchemy()
login_manager = LoginManager()
session_flask = Session()


def notfound(e):
    """404 template"""
    return render_template('404.html'), 404


def create_app():
    """Initialize core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    app.register_error_handler(404, notfound)

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session_flask.init_app(app)

    with app.app_context():
        from application.content.routes import content_bp
        from application.landing_page.routes import auth_bp

        # Registering Blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(content_bp)

        db.create_all()

        return app
