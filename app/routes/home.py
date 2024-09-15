from flask import Flask, Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    return 'Home'

def init(app: Flask):
    app.register_blueprint(home)
