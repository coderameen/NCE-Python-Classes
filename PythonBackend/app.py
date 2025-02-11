#Flask App
from flask import Flask

#initialize the Flask App
app = Flask(__name__)

#default route (route 1)
@app.route("/")
def home():
    return "This is my first landing page!!"

@app.route("/login")
def login():
    return "This is my login page!!"

@app.route("/service")
def service():
    return "This is my service page"

@app.route("/contact")
def contact():
    return "This is my contact page!!"


@app.route("/logout")
def logout():
    return "This is my Logout page"
if __name__=='__main__':
    app.run(debug=True, port=5001)