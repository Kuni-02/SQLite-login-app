from flask import Flask,request,render_template,url_for
app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/new")
def new():
    return render_template("makeacc.html")
    
if __name__=="__main__":
    app.run(debug=True)
