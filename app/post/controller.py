from flask import Blueprint, request, jsonify
from app.post.models import Post

POST = Blueprint('post', __name__, url_prefix='/api/v1/posts')


@POST.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    poster_id = request.form.get('poster_id')
    pst =  Post(title, content, poster_id)
    pst.createPost()
    return jsonify({"data": {"status": "success", "action": "create", "scope": "post"}}), 201

@POST.route('/<post_id>', methods=['GET'])
def getPostById(post_id):
    post = Post.getPostById(post_id)
    if post is None:
        return jsonify({"error": {"message": "wrong post id"}})
    return jsonify({"post": {"id": post.id, "title": post.title, "content": post.content, "poster": post.poster.name}})

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
