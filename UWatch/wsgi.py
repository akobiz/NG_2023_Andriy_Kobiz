from flask import Flask, render_template, redirect, url_for, session, request
import dbWorker
from commands import *

app = Flask(__name__)
app.config.from_object('config.Config')
dbWorker.configure_db(app)

@app.route('/')
def index():
    t = dbWorker.takeVideos()
    return render_template('index.html', t=t)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/upload')
        file = request.files['file']
        if file.filename.endswith('.mp4'):
            url = generateVideoURL()
            file.save(generateVideoPath(app.config['UPLOAD_FOLDER'], url + '.mp4'))
            dbWorker.addVideo(url)
        return redirect('/')
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/playback/<string:url>')
def playback(url):
    return render_template('playback.html')

if __name__ == "__main__":
    with app.app_context():
        print(dbWorker.checkVideos(app.config['UPLOAD_FOLDER']))
    app.run(host='0.0.0.0', port=5050)