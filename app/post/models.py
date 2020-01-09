from app import db
from app.user.models import UserModel

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    poster = db.relationship(UserModel, lazy='joined')

    def __init__(self, title='', content='', poster_id=''):
        self.title = title
        self.content = content
        self.poster_id = poster_id
    
    def createPost(self):
        db.session.add(self)
        db.session.commit()

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