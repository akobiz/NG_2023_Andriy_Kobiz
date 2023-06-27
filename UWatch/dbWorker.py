from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from commands import clearNoExistingVideos, randomizeVideos, deleteVideoFromServer
from datetime import datetime

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

def getUser(email):
    return Users.query.filter_by(email=email).first()

def getUserID(user_id):
    return Users.query.get(int(user_id))

def checkUserPassword(email):
    return Users.query.filter_by(email=email).with_entities(Users.password).first()

def checkUserExists(email):
    if Users.query.filter_by(email=email).first():
        return True
    else:
        return False

def addUser(email, password, channel_name):
    db.session.add(Users(email, channel_name, password))
    db.session.commit()

def takeVideos(orderByViews=False):
    if orderByViews == False:
        videos = Videos.query.all()
        randomizeVideos(videos)
    else:
        videos = Videos.query.order_by(Videos.views.desc()).all()
    return videos

def editVideo(video_url, name, description):
    record = Videos.query.filter_by(video_url=video_url).first()

    if record is not None:
        record.video_name = name
        record.description = description
        db.session.commit()

def deleteVideo(video_url, path):
    deleteVideoFromServer(video_url, path)
    db.session.query(Comments).filter_by(video_url=video_url).delete()
    db.session.query(Videos).filter_by(video_url=video_url).delete()
    db.session.commit()

def addVideo(url, fk_user_id, video_name, description, like=0, dislike=0, views=0):
    if video_name == "": 
        video_name = datetime.now().date()

    db.session.add(Videos(fk_user_id, url, video_name, like, dislike, views, description))
    db.session.commit()

def addComment(user_id, video_url, comment):
    db.session.add(Comments(user_id, video_url, comment, datetime.now().ctime()))
    db.session.commit()

def addView(video_url):
    record = Videos.query.filter_by(video_url=video_url).first()
    print('aaa')
    print(record, record.video_name, record.views)

    if record is not None:
        print(record.views)
        record.views = int(record.views) + 1
        db.session.commit()

def takeVideoToWatch(video_url):
    return Videos.query.filter_by(video_url=video_url).first()

def takeCommentsFromVideo(video_url):
    return Comments.query.filter_by(video_url=video_url).all()

def takeVideosFromUser(user_id):
    return Videos.query.filter_by(user_id=user_id).all()

def searchVideos(name:str):
    videos = Videos.query.all()
    similarVideos = videos.copy()
    for video in videos:
        if name.lower() not in video.video_name.lower():
            similarVideos.remove(video)
    randomizeVideos(videos)
    if len(videos) < 15:
        return videos, similarVideos
    else:
        return videos[:15], similarVideos