from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbconfig = 'postgresql://barryyt_cai:postgres@localhost:5432/firtpostgres'
app.config['SQLALCHEMY_DATABASE_URI'] = dbconfig

db = SQLAlchemy(app)

from .user.controller import USER
from .role.controller import ROLE
from .post.controller import POST

app.register_blueprint(USER)
app.register_blueprint(ROLE)
app.register_blueprint(POST)
