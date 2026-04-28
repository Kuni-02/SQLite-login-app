from flask import Flask,request,render_template,url_for
import sqlite3,os

app=Flask(__name__)

dbname=('test.db')
#テーブルの作成
def create_table():

    conn=sqlite3.connect(dbname,isolation_level=None)
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   """)
    conn.commit()
    conn.close()

#ユーザの追加
def add_user(email,password):
    #もしemailとかが未入力だった場合の処理
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO users(email,password) VALUES (?,?)",(email,password))
        conn.commit()
        return "success"
    except sqlite3.IntegrityError:
        return "false"
    finally:
        conn.close()

#ログイン判定
def check_login(email,password):
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email=? AND password=?",(email,password))
    row=cursor.fetchone()
    conn.close()
    return row

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        user=check_login(email,password)
        if user:
            return render_template("home.html")
        else:
            return "メールアドレスまたはパスワードがちがいます．"
    return render_template("login.html")

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        result=add_user(email,password)
        if result=="success":
            return render_template("login.html")
        else:
            return "このメールアドレスは既に使用されています．"
    else:
        return render_template("makeacc.html")
    
if __name__=="__main__":
    create_table()
    app.run(debug=True)
