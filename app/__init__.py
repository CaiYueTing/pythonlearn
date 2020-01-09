from flask import Blueprint, Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://barryyt_cai:postgres@localhost:5432/firtpostgres'

db.init_app(app)


from app.user.controller import USER
from app.role.controller import ROLE
from app.post.controller import POST


app.register_blueprint(USER)
app.register_blueprint(ROLE)
app.register_blueprint(POST)

