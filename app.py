from flask import Flask,request,render_template,url_for
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        PS=request.form["PS"]
    return render_template("login.html")

@app.route("/new")
def new():
    return render_template("makeacc.html")
    
if __name__=="__main__":
    app.run(debug=True)
