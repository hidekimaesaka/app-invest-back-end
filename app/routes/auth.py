from flask import Flask, Blueprint, jsonify, request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_access_token

from app.services.user import UserService


user_svc = UserService()

auth = Blueprint('auth', __name__)

@auth.route('/auth', methods=['POST'])
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')

    validated = user_svc.validate_user_credentials(username, password)
    
    if validated:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify(msg='Failed to login!'), 400

def init(app: Flask):
    app.register_blueprint(auth)
