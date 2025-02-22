from flask import Flask, render_template, request, redirect, url_for
from studentdatabase import conn,cursor
app = Flask(__name__)

#GET API
@app.route("/")
def home():
    cursor.execute("""SELECT * FROM students""")
    rows = cursor.fetchall()
    
    return render_template("index.html",rows = rows)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/adddb", methods=['GET','POST'])
def adddb():
    if request.method == 'POST':
        usn = request.form['usnbox']
        name = request.form['namebox']
        marks = request.form['marksbox']
        # print([usn,name,marks])
        cursor.execute("""INSERT INTO students(usn,name,marks) VALUES(?,?,?)""",(usn,name,marks))
        conn.commit()
        
    return redirect(url_for("home"))


@app.route("/update")
def update():
    return render_template("update.html")


@app.route("/updatedb", methods=['GET','POST'])
def updatedb():
    if request.method == 'POST':
        usn = request.form['usnbox']
        name = request.form['namebox']
        marks = request.form['marksbox']
        # breakpoint()
        cursor.execute("""UPDATE students SET name=?,marks=? WHERE usn=?""",(name,marks,usn))
        conn.commit()
    return redirect(url_for('home'))

@app.route("/delete/<usn>")
def delete(usn):
    cursor.execute("""DELETE FROM students WHERE usn=?""",(usn,))
    conn.commit()
    return redirect(url_for("home"))
if __name__== '__main__':
    app.run(debug=True)