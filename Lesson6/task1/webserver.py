from flask import Flask, render_template, redirect, request, url_for, session
from dbworker import *

DB_PATH = 'Lesson6/task1/news.db'

app = Flask("News", template_folder="C:/Users/User/Desktop/git/NG_2023_Andriy_Kobiz/Lesson6/task1/templates")

app.secret_key='123456'
@app.route('/', methods=['GET', 'POST'])
def index():
    news = takeNews(DB_PATH)
    if request.method == 'POST':
            id = request.form['news_id']
            return redirect(url_for('.edit', id=id))
    elif request.method == 'GET':
        return render_template('index.html', len = len(news), news=news)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        users = takeUsers(DB_PATH)
        for user in users:
            if username in user and user[2] == password:
                session['Auth'] = True
                return redirect('/')
    else:
        return render_template('login.html')

@app.route('/edit')
def edit():
    if session.get("Auth"):
        try:
            id = int(request.args['id'])
            news = takeNews(DB_PATH)[id]
            return render_template('edit.html', news=news)
        except:
            return render_template('edit.html', adding=True, news=0)
    else:
        return redirect('/login')

@app.route('/sendNews', methods=['POST'])
def sendNews():
    if request.method == "POST":
        if session.get("Auth"):
            id = request.form["id"]
            title = request.form["title"]
            author = request.form["author"]
            news = request.form["news"]

            if request.form['action'] == "add":
                addNews(DB_PATH, title, author, news)

            elif request.form['action'] == "update":
                print(id, title, author, news)
                editNews(DB_PATH, id, title, author, news)

            elif request.form['action'] == "delete":
                deleteNews(DB_PATH, id)
    else:
        return redirect('/login')

    return redirect('/')

if __name__ == "__main__":
    initTables(DB_PATH)
    app.run(host='0.0.0.0', port='3030')