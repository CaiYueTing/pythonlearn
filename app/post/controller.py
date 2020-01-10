from flask import Blueprint, request, jsonify
from app.post.models import Post

POST = Blueprint('post', __name__, url_prefix='/api/v1/posts')


@POST.route('/', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    poster_id = request.form.get('poster_id')
    pst = Post(title, content, poster_id)
    pst.createPost()
    message = {
        "data": {"status": "success", "action": "create", "scope": "post"}
    }
    return jsonify(message), 201


@POST.route('/<post_id>', methods=['GET'])
def getPostById(post_id):
    post = Post.getPostById(post_id)
    if post is None:
        return jsonify({"error": {"message": "wrong post id"}}), 404
    pst = {
        "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "poster": post.poster.name
            }
    }
    return jsonify(pst), 200


@POST.route("", methods=["GET"])
def searchByArgs():
    created_at = request.args.get("created_at", None)
    updated_at = request.args.get("updated_at", None)
    title = request.args.get("title", None)
    content = request.args.get("content", None)
    args = {
        "title": title,
        "content": content,
        "created_at": created_at,
        "updated_at": updated_at
    }
    posts = Post.getPostsByArgs(args)
    if posts is None:
        return jsonify({"error": {"message": "can't not find post"}}), 404
    data = {"data": []}
    for post in posts:
        pst = {
            "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "poster": post.poster.name
            }
        }
        data['data'].append(pst)
    return data, 200


@POST.route("/list", methods=["GET"])
def postsList():
    posts = Post.getAllPosts()
    data = {"data": []}
    for post in posts:
        pst = {
            "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "poster": post.poster.name
            }
        }
        data['data'].append(pst)
    return data, 200


@POST.route('/<post_id>', methods=["PATCH"])
def updatePostById(post_id):
    title = request.form.get('title')
    content = request.form.get('content')
    info = {"title": title, "content": content}
    uppst = Post.updatePostById(post_id, info)
    if uppst is None:
        return jsonify({"error": {"message": "wrong post id"}}), 404
    message = {
        "data": {"status": "success", "action": "update", "scope": "post"}
    }
    return jsonify(message), 200


@POST.route('/<post_id>', methods=["DELETE"])
def deletePostById(post_id):
    dpst = Post.deletePostById(post_id)
    if dpst is None:
        return jsonify({"error": {"message": "wrong post id"}}), 404
    message = {
        "data": {"status": "success", "action": "delete", "scope": "post"}
    }
    return jsonify(message), 200
