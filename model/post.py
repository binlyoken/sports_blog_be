from datetime import datetime
from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True)
    content = db.Column(db.Text)
    image = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.now())
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all,delete-orphan")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'),
        nullable=False)