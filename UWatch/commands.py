from uuid import uuid4
from os import path, listdir, remove as rm

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