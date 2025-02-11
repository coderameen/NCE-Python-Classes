#pip install flask
from flask import Flask,redirect, url_for

#initialize the flask app
app = Flask(__name__)

@app.route("/")
def myfirstpage():
    return "Main page"

@app.route("/home/<user>")
def home(user):
    return f"Wecome {user}"

@app.route("/service")
def service():
    return "This is my service page"

@app.route("/signup")
def signup():
    return "this is my registration page"

@app.route("/login")
def login():
    return "This is my login page!!!"

@app.route("/logout")
def logout():
    return redirect(url_for("login"))
if __name__=='__main__':
    app.run(debug=True)