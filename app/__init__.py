import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def generate_secret_key():
    return os.urandom(24)

def create_app(secret_key=None):
    app = Flask(__name__)

    # Configure the application
    if secret_key:
        app.config['SECRET_KEY'] = secret_key
    else:
        app.config['SECRET_KEY'] = generate_secret_key()

    # Set MySQL database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@127.0.0.1/grocery'

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Import models after db initialization to avoid circular import
    from . import models

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Apply CSRF protection to login and signup forms only
    @app.before_request
    def csrf_protect():
        if request.method == "POST" and request.endpoint in ['main.login', 'main.signup']:
            csrf.protect()

    return app
