from uuid import uuid4
from os import path, listdir, remove as rm
from werkzeug.security import generate_password_hash, check_password_hash
import cv2
import random

def generateVideoURL():
    return (uuid4().hex)

def generateVideoPath(folder, url):
    return path.join(folder, url)

def clearNoExistingVideos(videos, uploadPath):
    existingVideos = []
    videosCopy = []
    for file in listdir(uploadPath):
        for video in videos:
            
            if len(videosCopy) != len(videos):
                videosCopy.append(video[0])
            
            if file[:-4] == video[0]:
                existingVideos.append(file[:-4])

    notExistingVideos = [e for e in videosCopy if e not in existingVideos]
    for file in notExistingVideos:
        try:
            rm(uploadPath + file + 'mp4')
        except Exception as e:
            print(e)
    
    return notExistingVideos

def generatePreview(video, folder):
    print(video)
    openVideo = cv2.VideoCapture(folder + video + '.mp4')
    openVideo.set(cv2.CAP_PROP_POS_MSEC, 2*1000)

    success, frame = openVideo.read()
    
    if not success:
        print(video + ': have not created thumbnail for video.')

    frame = cv2.resize(frame, (450, 325))
    cv2.imwrite(folder + video + '.jpg', frame)
    openVideo.release()

def hashPass(password):
    return generate_password_hash(password)

def checkPassValid(hashPsw, psw):
    return check_password_hash(hashPsw, psw)

def checkPathIsValid(pth):
    return path.exists('static/' + pth)

def randomizeVideos(videos):
    random.shuffle(videos)

def deleteVideoFromServer(video, pth):
    rm(pth + video + ".mp4")