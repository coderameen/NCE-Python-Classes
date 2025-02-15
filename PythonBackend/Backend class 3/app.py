from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", content=['apple','mango','banana'])

@app.route("/page2")
def page2():
    return render_template("index2.html", studentdetail = {'usn':'CS01','name':'Alen','marks':97})

if __name__=='__main__':
    app.run(debug=True)