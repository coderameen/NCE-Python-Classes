from flask import Flask, render_template, request

app = Flask(__name__)

#GET API
@app.route("/")
def home():
    return render_template("index.html")


#POST API
@app.route("/addapi", methods=['GET','POST'])
def addapi():
    if request.method == 'POST':
        n1 = request.form['num1']
        n2 = request.form['num2']
        # print(n1, n2)
        if n1 != '' and n2 != '':
            res = int(n1) + int(n2)
        return f"The sum is {res}"
    

if __name__=='__main__':
    app.run(debug=True)