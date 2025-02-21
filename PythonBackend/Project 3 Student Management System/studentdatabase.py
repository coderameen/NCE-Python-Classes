import sqlite3
conn = sqlite3.connect("schooldb.db", check_same_thread=False)
print("DB Crearted successfully!!")
cursor = conn.cursor()
#create table: student(usn,Name, Marks)
cursor.execute("""CREATE TABLE IF NOT EXISTS students(usn TEXT PRIMARY KEY, name TEXT NOT NULL, marks TEXT NOT NULL)""")
conn.commit()

# #insert data
# cursor.execute("""INSERT INTO students(usn,name,marks) VALUES(?,?,?)""",("CS01","Alen",89))
# conn.commit()
# cursor.execute("""INSERT INTO students(usn,name,marks) VALUES(?,?,?)""",("CS02","bob",79))
# conn.commit()

