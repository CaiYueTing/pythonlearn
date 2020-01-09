from flask import Flask, request, render_template, jsonify, Blueprint
from app.user.models import UserModel, Role
import json

USER = Blueprint('user', __name__, url_prefix='/api/v1/users')
# api route default url


@USER.route('/create', methods=['POST'])
def createUser():
    name = request.form.get('name')
    email = request.form.get('email')
    role_id = request.form.get('role')
    usr = UserModel(name, email, role_id)
    usr.create()
    return jsonify({"data": {"status": "success", "action": "create", "scope": "user :" + name}}), 201


@USER.route('/<user_id>', methods=["GET"])
def user(user_id):
    user = UserModel.getUserById(user_id)
    if user is None:
        return jsonify({"error": {"message": "wrong user id"}})
    return jsonify({"user": {"id": user.id, "name": user.name, "email": user.email, "role": user.rolename.role}}), 200


@USER.route('/update/<user_id>', methods=["PATCH"])
def userUpdate(user_id):
    name = request.form.get('name')
    email = request.form.get('email')
    role_id = request.form.get('role')
    info = {"name": name, "email": email, "role_id": role_id}
    uuser = UserModel.updateUserById(user_id, info)
    if uuser is None:
        return jsonify({"error": {"message": "wrong user id"}})
    return jsonify({"data": {"status": "success", "action": "update", "scope": "user :" + user_id}}), 200


@USER.route('/delete/<user_id>', methods=["DELETE"])
def userDelete(user_id):
    duser = UserModel.deleteUserById(user_id)
    if duser is None:
        return jsonify({"error": {"message": "wrong user id"}})
    return jsonify({"data": {"status": "success", "action": "delete", "scope": "user :" + user_id}}), 200


@USER.route('', methods=["GET"])
def allusers():
    users = UserModel.getAllUsers()
    if users is None:
        return jsonify({"error": {"message": "wrong user id"}})

    data = {"data": []}
    for user in users:
        usr = {
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.rolename.role
            }
        }
        data["data"].append(usr)

    return jsonify(data), 200
