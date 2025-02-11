from flask import Flask, render_template

app = Flask(__name__)

#GET API
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
if __name__=='__main__':
    app.run(debug=True)