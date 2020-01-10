from app import db


class DataTimeBase(object):
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, onupdate=db.func.now(), default=db.func.now()
    )
