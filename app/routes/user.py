from flask import Flask, Blueprint, request, jsonify

from flask_jwt_extended import jwt_required

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


@user.route('/user/update', methods=['POST'])
@jwt_required()
def update_user():
    user = request.get_json()

    updated = user_repo.update_user(user)
    if not updated:
        return jsonify(msg='Could not update user!'), 400

    return jsonify(msg='User updated!'), 200


@user.route('/user/delete', methods=['POST'])
@jwt_required()
def delete_user():
    request_data = request.get_json()
    username = request_data['username']

    deleted = user_repo.delete_user(username)
    if not deleted:
        return jsonify(msg='Could not delete user!'), 400
    
    return jsonify(msg='User deleted!'), 200


@user.route('/user/get', methods=['POST'])
@jwt_required()
def get_user():
    request_data = request.get_json()

    try:
        key = request_data['username']
        user = user_repo.get_user_by_username(key)
        if not user:
            return jsonify(msg='User not found!'), 400

        return jsonify(
            name = user.name,
            email = user.email,
            username = user.username
        ), 200

    except KeyError:
        return jsonify(msg='Please provide an username or email'), 400


def init(app: Flask):
    app.register_blueprint(user)
