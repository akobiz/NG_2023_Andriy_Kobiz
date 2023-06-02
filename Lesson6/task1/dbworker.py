import sqlite3
from datetime import datetime

def initConnection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("DATABASE CONNECTION OK!\n")
    except Exception as e:
        print("DATABASE NOT CONNECTED: " + str(e))
    return conn

def initTables(path):
    with initConnection(path) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users" 
                    "(id integer PRIMARY KEY,"
                    "login text NOT NULL,"
                    "password text NOT NULL)")
        conn.execute("CREATE TABLE IF NOT EXISTS news"
                    "(id integer PRIMARY KEY,"
                    "title text NOT NULL,"
                    "author text NOT NULL,"
                    "data text NOT NULL,"
                    "information text NOT NULL)")
        
        if len(list(conn.execute("SELECT login FROM users WHERE login IS NOT NULL"))) == 0:
            addUser(path, 'admin', 'admin')
            addUser(path, '123', '123')

        if len(list(conn.execute("SELECT id FROM news"))) == 0:
            addNews(path, "Example", "Unknown", "Some text here.")

        print("Users registered:", len(list(conn.execute("SELECT login FROM users WHERE login IS NOT NULL"))))
        conn.commit()

def addUser(path, username, password):
    with initConnection(path) as conn:
        conn.execute("INSERT INTO users (login, password) VALUES ('{}','{}')".format(username, password))
        conn.commit()

def addNews(path, title, author, information):
    with initConnection(path) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO news (title, author, data, information) VALUES ('{}','{}','{}','{}')" \
                         .format(title, author, datetime.now().date(), information))
        conn.commit()
        cur.close()

def deleteNews(path, id):
    with initConnection(path) as conn:
        conn.execute("DELETE FROM news WHERE id = ({})".format(id))
        conn.commit()
    print(f"[{datetime.now().time()}]News with id[{id}] was deleted.")

def editNews(path, id, title, author, information):
    with initConnection(path) as conn:
        date = datetime.now().date()
        cur = conn.cursor()
        query = "UPDATE news SET title = ?, author = ?, data = ?, information = ? WHERE id = ?"
        col = (title, author, date, information, id)
        cur.execute(query, col)
        conn.commit()
        cur.close()
    
    print(f"\n\n[{datetime.now().time()}]: News with id[{id}] was updated.\n\n")

def takeNews(path):
    with initConnection(path) as conn:
        return list(conn.execute("SELECT * FROM news"))
    
def takeUsers(path):
    with initConnection(path) as conn:
        return list(conn.execute("SELECT * FROM users"))
