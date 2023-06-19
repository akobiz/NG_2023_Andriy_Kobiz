from dbWorker import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    channel_name = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, channel_name, password):
        self.email = email
        self.channel_name = channel_name
        self.password = password

    def __repr__(self):
        return f"Email: {self.email}, Channel Name: {self.channel_name}, Password: {self.password}"

class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(15), unique=True, nullable=False)
    like = db.Column(db.Integer, nullable=False)
    dislike = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __init__(self, video_url, like, dislike, views):
        self.video_url = video_url
        self.like = like
        self.dislike = dislike
        self.views = views

    def __repr__(self):
        repre = []
        return str([self.id, self.video_url, self.like, self.dislike, self.views])