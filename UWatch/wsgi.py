from flask import Flask, render_template, redirect, url_for, session, request, g, jsonify, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
import dbWorker as dbw
from commands import *

app = Flask(__name__)
app.config.from_object('config.Config')
login_manager = LoginManager()

dbw.configure_db(app)

login_manager.init_app(app)
login_manager.login_view = 'sign'

@login_manager.user_loader
def user_loader(user_id):
    return dbw.getUserID(user_id)

@app.route('/')
def index():
    try:
        if request.args['order-by'] == 'views':
            videos = dbw.takeVideos(True)
        else:
            videos = dbw.takeVideos(False)
    except:
        videos = dbw.takeVideos(False)
    return render_template('index.html', videos=videos)

@app.route('/search')
def search():
    searched = str(request.args['srch'])
    videos, similarVideos = dbw.searchVideos(searched)
    if len(similarVideos) < 1:
        return render_template('search.html', videos=videos)
    return render_template('search.html', videos=videos, similarVideos=similarVideos)

@app.route('/panel/<string:url>', methods=['GET', 'POST'])
@login_required
def edit(url):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['descr']

        if 'file' in request.files:
            file = request.files['file']
            if file.filename.endswith('.jpg'):
                file.save(generateVideoPath(app.config["UPLOAD_FOLDER"] + url + '.jpg'))

        dbw.editVideo(url, name, description)
        return redirect('/panel')
    
    return render_template('editing.html', url=url)

@app.route('/panel/delete', methods=['POST'])
@login_required
def delete():
    if request.form['action'] == 'delete':
        dbw.deleteVideo(request.form['url'], app.config["UPLOAD_FOLDER"])
    return redirect('/panel')

@app.route('/panel')
@login_required
def panel():
    videos = dbw.takeVideosFromUser(current_user.id)
    print(videos)
    return render_template('panel.html', videos=videos)

@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/upload')
        file = request.files['file']
        if file.filename.endswith('.mp4'):
            url = generateVideoURL()
            video_name = request.form['name']
            poster = request.files['poster']
            description = request.form['descr']
            file.save(generateVideoPath(app.config['UPLOAD_FOLDER'], url + '.mp4'))
            if poster.filename.endswith('.jpg'):
                poster.save(generateVideoPath(app.config['UPLOAD_FOLDER'], url + '.jpg'))
            else:
                generatePreview(url, app.config['UPLOAD_FOLDER'])

            dbw.addVideo(url, video_name=video_name, fk_user_id=current_user.id, description=description)
        return redirect('/')
    
    elif request.method == 'GET':
        print(current_user.id)
        return render_template('upload.html')

@app.route('/playback/<string:url>')
def playback(url):
    poster = 'uploads/' + url + '.jpg'
    comments = dbw.takeCommentsFromVideo(url)
    video = dbw.takeVideoToWatch(url)
    dbw.addView(url)
    url = 'uploads/' + url + '.mp4'
    if checkPathIsValid(poster):
        return render_template('playback.html', url=url, poster=poster, comments=comments, video=video)
    return render_template('playback.html', url=url, comments=comments, video=video)

@app.route('/leaveComment', methods=['POST'])
def leaveComment():
    id = request.form['user']
    url = request.form['url'][8:-4]
    comment = request.form['comment']
    if comment != "":
        dbw.addComment(id, url, comment)
    return redirect('/playback/' + url)

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        if request.form['btn'] == 'signin':
            email = request.form['email']
            password = request.form['password']
            if dbw.checkUserExists(email) and checkPassValid(dbw.checkUserPassword(email)[0], password):
                login_user(dbw.getUser(email))
                return redirect('/')
            else:
                flash("Email doesn't exists or password are not correct!")
                return redirect('/sign')
    return render_template('sign.html')

@app.route('/sign/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        print(request.form)
        if request.form['btn'] == 'reg':
            email = request.form['email']
            psw = request.form['psw']
            psw_check = request.form['psw_check']
            channel_name = request.form['channel']

            if not dbw.checkUserExists(email) and psw == psw_check:
                dbw.addUser(email, hashPass(psw), channel_name)
                return redirect('/sign')
            elif dbw.checkUserExists(email):
                flash("Email is already registered! Try register with other email.")
            else:
                flash("The password does not match.")
            return redirect('/sign/registration')
    return render_template('registration.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        dbw.checkVideos(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=5050)