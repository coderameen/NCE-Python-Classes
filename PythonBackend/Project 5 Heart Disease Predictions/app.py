from flask import Flask, render_template, redirect, request,url_for

app = Flask(__name__)

import pickle

model = pickle.load(open('model.pkl','rb'))
#GET API
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        n1 = request.form['inp1box']
        n2 = request.form['inp2box']
        n3 = request.form['inp3box']
        n4 = request.form['inp4box']
        n5 = request.form['inp5box']
        n6 = request.form['inp6box']
        n7 = request.form['inp7box']
        n8 = request.form['inp8box']
        n9 = request.form['inp9box']
        n10 = request.form['inp10box']
        n11 = request.form['inp11box']
        n12 = request.form['inp12box']
        n13 = request.form['inp13box']
        
        #predict the output
        pred = model.predict([[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13]])
        if pred[0] == 1:
            # return "Patient has heart disease"
            msg = "Patient has heart disease"
            return render_template("index.html",msg=msg)
            
        else:
            # return "He dosen't has heart disease"
            msg = "He dosen't has heart disease"
            return render_template("index.html", msg=msg)
        
if __name__=='__main__':
    app.run(debug=True)