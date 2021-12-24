import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'static'
app.config["ALLOWED_EXTENSIONS"] = set(['png', 'jpg', 'jpeg'])
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

api = Api(app)

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory("/home/winsnyder/projects/compare_car_be/static",
                               filename, as_attachment=True)

from model.account import Account
from model.post import Post
from model.comment import Comment
from model.topic import Topic
from app import routes