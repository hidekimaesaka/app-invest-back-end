from os import getenv

from flask import Flask, Blueprint, jsonify, request

from flask_jwt_extended import create_access_token

from flask_jwt_extended import create_access_token


auth = Blueprint('auth', __name__)

@auth.route('/auth', methods=['POST'])
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')

    api_username = getenv('API_USERNAME')
    api_password = getenv('API_PASSWORD')

    if username != api_username or password != api_password:
        return jsonify(msg='Login failed!'), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


def init(app: Flask):
    app.register_blueprint(auth)
