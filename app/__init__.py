from flask import Flask

from app.config import load_config

from app.routes import home, user, auth

from app.extensions import jwt

def create_app():

    app = Flask(__name__)
    load_config(app)

    jwt.init(app)

    home.init(app)
    auth.init(app)
    user.init(app)

    return app
