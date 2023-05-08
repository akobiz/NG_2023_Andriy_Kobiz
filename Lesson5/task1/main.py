from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask("Chat", template_folder="C:/Users/User/Desktop/git/NG_2023_Andriy_Kobiz/Lesson5/task1/templates")

users = {"admin": "admin"}
messages = ["[00.00.00]admin: hello", "[00.00.01]admin: bye"]

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/auth', methods=['POST'])
def authorization():
    global username
    username = request.form['username']
    if username in users and users[username] == request.form['psw']:
        return redirect('/chat')
    else:
        return redirect('/')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['psw']
        users[username] = password
        print(users)
        return redirect('/')
    elif request.method == 'GET':
        return render_template('register.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        try:
            makeMessage(username, message=request.form['message'])
        except Exception as e:
            makeMessage(message=request.form['message'])
        return redirect('/chat')
    elif request.method == "GET":
        return render_template('chat.html', messages=messages)

def makeMessage(username='unk', message="unk"):
    messages.append(f"[{str(datetime.now())[11:19]}]{username}: {message}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="3030")