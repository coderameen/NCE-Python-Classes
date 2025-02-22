from flask import Flask,render_template,request,redirect,url_for
from database import conn,cursor

app = Flask(__name__)

@app.route("/")
def home():
    cursor.execute("""SELECT * FROM doctors""")
    rows = cursor.fetchall()
    
    return render_template("index.html", rows = rows)


@app.route("/patientdata", methods=['GET','POST'])
def patientdata():
    if request.method == 'POST':
        patient_name = request.form['pnamebox']
        book_time = request.form['tbox']
        doctor_name = request.form['pdbox']
        # print([patient_name,book_time,doctor_name])
        cursor.execute("""INSERT INTO patients(p_name,p_time,d_name) VALUES(?,?,?)""",(patient_name,book_time,doctor_name))
        conn.commit()
        return render_template("index.html", result = "Doctor has appointed Successfuly!!!")



@app.route("/doctordashboard")
def doctordashboard():
    return render_template("doctordashboard.html")


@app.route("/view_patient", methods=['GET','POST'])
def view_patient():
    if request.method == 'POST':
        doctor_name = request.form['docbox']
        cursor.execute("""SELECT p_id,p_name,p_time FROM patients WHERE d_name=? """,(doctor_name,))
        rows = cursor.fetchall()
        
        return render_template("doctordashboard.html", rows = rows)
        
if __name__=='__main__':
    app.run(debug=True)