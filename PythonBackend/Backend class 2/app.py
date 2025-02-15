
#BACKEND
from flask import Flask, render_template

app = Flask(__name__)

#route (GET API)
@app.route("/<user>")
def home(user):
    return  render_template("index.html", content = user  )
    # return  f"welcome {user}"

if __name__=='__main__':
    app.run(debug=True)

