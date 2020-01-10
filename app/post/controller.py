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
        return jsonify({"error": {"message": "wrong post id"}})
    pst = {
        "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "poster": post.poster.name
            }
    }
    return jsonify(pst), 200


@POST.route('/list', methods=["GET"])
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
    return data


@POST.route('/<post_id>', methods=["PATCH"])
def updatePostById(post_id):
    title = request.form.get('title')
    content = request.form.get('content')
    info = {"title": title, "content": content}
    uppst = Post.updatePostById(post_id, info)
    if uppst is None:
        return jsonify({"error": {"message": "wrong post id"}})
    message = {
        "data": {"status": "success", "action": "create", "scope": "post"}
    }
    return jsonify(message), 200


@POST.route('/<post_id>', methods=["DELETE"])
def deletePostById(post_id):
    dpst = Post.deletePostById(post_id)
    if dpst is None:
        return jsonify({"error": {"message": "wrong post id"}})
    message = {
        "data": {"status": "success", "action": "create", "scope": "post"}
    }
    return jsonify(message), 200
