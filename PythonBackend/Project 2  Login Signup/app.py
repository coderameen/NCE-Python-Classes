from flask import Flask, render_template, request
from database import conn,cursor
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/addsignupdata", methods=['GET','POST'])
def addsignupdata():
    if request.method == 'POST':
        username = request.form['ubox']
        password = request.form['pbox']
        repassword = request.form['rpbox']
        if password == repassword:
            # print([username,password])
            cursor.execute("""INSERT INTO register(username,password) VALUES(?,?)""",(username,password))
            conn.commit()
        else:
            return "Password dosen't Matches"
    return "User registed Successfully"


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logindb", methods=['GET','POST'])
def logindb():
    if request.method == 'POST':
        un  = request.form['ubox']
        pwd = request.form['pbox']
        # print([un,pwd])
        cursor.execute("""SELECT username FROM register""")
        rows = cursor.fetchall()
        # print(rows)#[('text',), ('saniya',), ('gulfam',)] , but I need [text,saniya,gulfam]
        db_users = []
        for row in rows:
            db_users.append(row[0])
     
            
        # print(arr)#['text', 'saniya', 'gulfam']
        if un in db_users:
            cursor.execute("""SELECT password FROM register WHERE username=?""",(un,))
            db_pwd = cursor.fetchone()
          
            if pwd == db_pwd[0]:
                return render_template("dashboard.html")
            else:
                return "invalid password!!"
        else:
            return "Invalid Username"
        
        
    return "sdfkjhs"
    
if __name__=='__main__':
    app.run(debug=True)