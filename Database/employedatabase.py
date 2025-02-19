import sqlite3

#create database
conn = sqlite3.connect("company.db")

#cursor
cursor = conn.cursor()

#Create Table - Department
cursor.execute("""CREATE TABLE IF NOT EXISTS Department(dept_id INTEGER  PRIMARY KEY AUTOINCREMENT, dept_name TEXT NOT NULL)""")
#Create Table - Employee with Foreign key reference to Department
cursor.execute("""CREATE TABLE IF NOT EXISTS Employees(emp_id INTEGER PRIMARY KEY AUTOINCREMENT, emp_name TEXT NOT NULL, dept_id INTEGER, FOREIGN KEY (dept_id) REFERENCES Department(dept_id) ON DELETE CASCADE)""")
conn.commit()
print("Table created successfully!!")


#insert data - Department
# cursor.execute("""INSERT INTO Department(dept_name) VALUES(?)""",("HR",))
# cursor.execute("""INSERT INTO Department(dept_name) VALUES(?)""",("SOFTWARE",))
# cursor.execute("""INSERT INTO Department(dept_name) VALUES(?)""",("HARDWARE",))
# conn.commit()

# print("data inserted successfully")

#insert data - Employees
# cursor.execute("""INSERT INTO Employees(emp_name,dept_id) VALUES(?,?)""",("Alen",1))
# cursor.execute("""INSERT INTO Employees(emp_name,dept_id) VALUES(?,?)""",("Saniya",2))
# cursor.execute("""INSERT INTO Employees(emp_name,dept_id) VALUES(?,?)""",("Gulfam",3))
# conn.commit()
# print("data inserted successfully")


#Read data - read only employee name, department name
cursor.execute("""SELECT Employees.emp_name, Department.dept_name FROM Employees JOIN Department ON Employees.dept_id = Department.dept_id""")
rows = cursor.fetchall()
# print(rows)
for row in rows:
    print(row)
    
#Delete Department (CASCADE Effect)
#IF YOU DELETE A Department, all associated employees will also be deleteed due to on delte cascade

cursor.execute("""DELETE FROM Department WHERE dept_id=?""",(1,))
conn.commit()


#
cursor.execute("""SELECT Employees.emp_name, Department.dept_name FROM Employees JOIN Department ON Employees.dept_id = Department.dept_id""")
rows = cursor.fetchall()
# print(rows)
for row in rows:
    print(row)