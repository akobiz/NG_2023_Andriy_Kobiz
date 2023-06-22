from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from commands import clearNoExistingVideos
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

def addUser(email, password, channel='Andrew'):
    db.session.add(Users(email, channel, password))
    db.session.commit()

def takeVideos():
    return Videos.query.all()

def addVideo(url, fk_user_id, video_name, like=0, dislike=0, views=0):
    if video_name == "": 
        video_name = datetime.now().date()
        
    db.session.add(Videos(fk_user_id, url, video_name, like, dislike, views))
    db.session.commit()
