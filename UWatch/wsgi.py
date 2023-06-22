from flask import Flask, render_template, redirect, url_for, session, request, g
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
    t = dbw.takeVideos()
    return render_template('index.html', t=t)

@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/upload')
        file = request.files['file']
        if file.filename.endswith('.mp4'):
            url = generateVideoURL()
            file.save(generateVideoPath(app.config['UPLOAD_FOLDER'], url + '.mp4'))
            dbw.addVideo(url)
        return redirect('/')
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/playback/<string:url>')
def playback(url):
    return render_template('playback.html', url='uploads/' + url + '.mp4', poster='uploads/' + url + '.jpg')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        if request.form['btn'] == 'signin':
            email = request.form['email']
            password = request.form['password']
            if dbw.checkUserExists(email) and checkPassValid(dbw.checkUserPassword(email)[0], password):
                login_user(dbw.getUser(email))
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

            if not dbw.checkUserExists(email) and psw == psw_check:
                dbw.addUser(email, hashPass(psw))
            else: print("EXISTS")
            return redirect('/sign')
    return render_template('registration.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        print(dbw.checkVideos(app.config['UPLOAD_FOLDER']))
    app.run(host='0.0.0.0', port=5050)