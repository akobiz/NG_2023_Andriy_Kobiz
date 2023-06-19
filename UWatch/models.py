from dbWorker import db

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