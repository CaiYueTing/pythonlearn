from app import db
from app.role.models import Role


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(
        'role.id', ondelete="CASCADE"), nullable=False)
    rolename = db.relationship(Role, lazy='joined')

    def __init__(self, name='', email='', role_id=''):
        self.name = name
        self.email = email
        self.role_id = role_id

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def updateUserById(cls, id, info):
        usr = cls.query.filter(User.id == id).first()
        if usr is None:
            return None
        usr.name = usr.name if info['name'] is None else info['name']
        usr.email = usr.email if info['email'] is None else info['email']
        if info['role_id'] is None:
            usr.role_id = usr.role_id
        else:
            usr.role_id = info['role_id']

        db.session.commit()
        return "success"

    @classmethod
    def deleteUserById(cls, id):
        usr = cls.query.filter(User.id == id).first()
        if usr is None:
            return None
        db.session.delete(usr)
        db.session.commit()
        return 'success'

    @classmethod
    def getUserById(cls, findid):
        usr = cls.query.join(Role).filter(User.id == findid)\
                    .filter(User.role_id == Role.id).first()
        # usr = cls.query.get(findid)
        return usr

    @classmethod
    def getAllUsers(cls):
        users = cls.query.join(Role).filter(User.role_id == Role.id).all()
        return users

    def __repr__(self):
        return "<User %s>" % self.rolename.role
