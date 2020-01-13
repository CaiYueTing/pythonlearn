from app import db
from app.user.models import User
from app.model.datetime import DataTimeBase


class Post(DataTimeBase, db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    poster = db.relationship(User, lazy='joined')

    def __init__(self, title='', content='', poster_id=''):
        self.title = title
        self.content = content
        self.poster_id = poster_id

    def createPost(self):
        db.session.add(self)
        db.session.commit()
        return self.title

    @classmethod
    def getPostsByUser(cls, userid):
        posts = cls.query.filter(Post.poster_id == userid).all()
        if posts is None:
            return None
        return posts

    @classmethod
    def getPostById(cls, id):
        post = cls.query.filter(Post.id == id).first()
        if post is None:
            return None
        return post

    @classmethod
    def getPostsByUserArg(cls, id, args):
        created_at = args.get("created_at", None)
        updated_at = args.get("updated_at", None)
        title = args.get("title", None)
        content = args.get("content", None)
        post = cls.query.filter(Post.poster_id == id)
        if created_at is not None:
            post.filter(Post.created_at == created_at)
        if updated_at is not None:
            post.filter(Post.updated_at == updated_at)
        if title is not None:
            post.filter(Post.title == title)
        if content is not None:
            post.filter(Post.content == content)
        psts = post.all()
        return psts

    @classmethod
    def getAllPosts(cls):
        posts = cls.query.all()
        return posts

    @classmethod
    def updatePostById(cls, id, info):
        post = cls.query.filter(Post.id == id).first()
        if post is None:
            return None
        post.title = info['title'] if info['title'] else post.title
        post.content = info['content'] if info['content'] else post.content
        db.session.commit()
        return post

    @classmethod
    def deletePostById(cls, id):
        post = cls.query.filter(Post.id == id).first()
        if post is None:
            return None
        db.session.delete(post)
        db.session.commit()
        return 'success'

    def __repr__(self):
        return "<Post %s>" % self.title
