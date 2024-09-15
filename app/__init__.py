from flask import Flask

from app.config import load_config
load_config()

from app.routes import home, user


def create_app():

    app = Flask(__name__)

    home.init(app)

    user.init(app)

    return app
