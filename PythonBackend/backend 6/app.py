from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


model = pickle.load(open('model.pkl','rb'))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predictapi", methods=['GET','POST'])
def predictapi():
    if request.method == 'POST':
        sh = request.form['sh']
        ph = request.form['ph']
        pred = model.predict([[sh,ph]])
        print(pred)
        # return f"The Predicted cgpa of student is: {pred}"
        return render_template("index.html", content = pred[0])

if __name__=='__main__':
    app.run(debug=True)