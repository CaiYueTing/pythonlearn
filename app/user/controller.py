from flask import Blueprint, request, jsonify
from app.user.models import User
from app.post.models import Post

USER = Blueprint('user', __name__, url_prefix='/api/v1/users')
# api route default url


@USER.route('/', methods=['POST'])
def createUser():
    name = request.form.get('name')
    email = request.form.get('email')
    role_id = request.form.get('role')
    usr = User(name, email, role_id)
    id = usr.create()
    message = {
        "data": {
            "status": "success",
            "action": "create",
            "scope": "user :" + str(id)
        }
    }
    return jsonify(message), 201


@USER.route('/<user_id>', methods=["GET"])
def getUserById(user_id):
    user = User.getUserById(user_id)
    if user is None:
        return jsonify({"error": {"message": "wrong user id"}}), 404
    message = {
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.rolename.role
        }
    }
    return jsonify(message), 200


@USER.route('/<user_id>/posts', methods=["GET"])
def getPostsByUser(user_id):
    created_at = request.args.get('created_at', None)
    updated_at = request.args.get('updated_at', None)
    title = request.args.get('title', None)
    content = request.args.get('content', None)
    args = {
        "created_at": created_at,
        "updated_at": updated_at,
        "title": title,
        "content": content
    }
    posts = Post.getPostsByUserArg(user_id, args)

    # posts = Post.getPostsByUser(user_id)
    if posts is None:
        return jsonify({"error": {"message": "wrong user id"}}), 404

    data = {"data": []}
    for post in posts:
        pst = {
            "post_id": post.id,
            "title": post.title,
            "content": post.content,
            "poster": post.poster.name
        }
        data["data"].append(pst)

    return jsonify(data), 200


@USER.route('/<user_id>', methods=["PATCH"])
def updatePostById(user_id):
    name = request.form.get('name')
    email = request.form.get('email')
    role_id = request.form.get('role')
    info = {"name": name, "email": email, "role_id": role_id}
    uuser = User.updateUserById(user_id, info)
    if uuser is None:
        return jsonify({"error": {"message": "wrong user id"}}), 404
    message = {
        "data": {
            "status": "success",
            "action": "update",
            "scope": "user :" + user_id
        }
    }
    return jsonify(message), 200


@USER.route('/<user_id>', methods=["DELETE"])
def deleteUserById(user_id):
    duser = User.deleteUserById(user_id)
    if duser is None:
        return jsonify({"error": {"message": "wrong user id"}}), 404
    message = {
        "data": {
            "status": "success",
            "action": "delete",
            "scope": "user :" + user_id
        }
    }
    return jsonify(message), 204


@USER.route('/', methods=["GET"])
def getAllUsers():
    users = User.getAllUsers()
    if users is None:
        return jsonify({"error": {"message": "wrong user id"}}), 404

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
