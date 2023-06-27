from dbWorker import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    channel_name = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(100))

    videos = db.relationship('Videos', backref='user', lazy=True)
    #comments = db.relationship('Comments', backref='user', lazy=True)

    def __init__(self, email, channel_name, password):
        self.email = email
        self.channel_name = channel_name
        self.password = password

    def __repr__(self):
        return f"Email: {self.email}, Channel Name: {self.channel_name}, Password: {self.password}"

class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), name='fk_user_id')
    video_url = db.Column(db.String(15), unique=True, nullable=False)
    video_name = db.Column(db.String(45), nullable=False)
    like = db.Column(db.Integer, nullable=False)
    dislike = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

    #comments = db.relationship('Comments', backref='video', lazy=True)

    def __init__(self, user_id, video_url, video_name, like, dislike, views, description):
        self.user_id = user_id
        self.video_url = video_url
        self.video_name = video_name
        self.like = like
        self.dislike = dislike
        self.views = views
        self.description = description

    def __repr__(self):
        return str([self.id, self.video_url, self.like, self.dislike, self.views])
    
class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    video_url = db.Column(db.String(15), db.ForeignKey('videos.video_url'), nullable=False)
    comment = db.Column(db.Text)
    date = db.Column(db.String(15))

    user = db.relationship('Users', backref='user_comments')
    video = db.relationship('Videos', backref='videos_comments')

    def __init__(self, user_id, video_url, comment, date):
        self.user_id = user_id
        self.video_url = video_url
        self.comment = comment
        self.date = date