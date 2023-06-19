from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from commands import clearNoExistingVideos

db = SQLAlchemy()
migrate = Migrate()

def configure_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

from models import *

def checkVideos(uploadPath):
    video = Videos.query.with_entities(Videos.video_url).all()
    notExistingVideos = clearNoExistingVideos(video, uploadPath)

    for vid in notExistingVideos:
        checkVid = Videos.query.filter_by(video_url=vid).first()
        if checkVid:
            db.session.delete(checkVid)
            db.session.commit()
            print("Video deleted:" + vid)


def takeVideos():
    return Videos.query.all()

def addVideo(url, like=0, dislike=0, views=0):
    db.session.add(Videos(url, like, dislike, views))
    db.session.commit()
