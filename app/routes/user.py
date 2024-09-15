from flask import Flask, Blueprint, request, jsonify

from app.repository.user import UserRepository

user = Blueprint('user', __name__)

user_repo = UserRepository()


@user.route('/user/create', methods=['POST'])
def create_user():
    user = request.get_json()

    created = user_repo.add_user(user)
    if not created:
        return jsonify(msg='Username or email already taken'), 400

    return jsonify(msg='User created!'), 200


def init(app: Flask):
    app.register_blueprint(user)
