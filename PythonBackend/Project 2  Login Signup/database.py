import sqlite3

conn = sqlite3.connect("signupdb.db", check_same_thread=False)
print("db is created successfully")

cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS register(username TEXT NOT NULL, password TEXT NOT NULL)""")
conn.commit()
print("Table created succesfully!")

#insert data
# cursor.execute("""INSERT INTO register(username,password) VALUES(?,?)""",("text","test@123"))
# conn.commit()
# print("data inserted success")