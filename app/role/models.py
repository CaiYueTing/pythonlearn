from app import db

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)
    # aff = db.relationship("UserModel", backref="user", lazy='dynamic')
    
    def __init__(self, role):
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role
        }

    @classmethod
    def getRoleById(cls, id):
        role = cls.query.filter(Role.id == id).one()
        return role

    def __repr__(self):
        return "<Role: %s>" % self.role