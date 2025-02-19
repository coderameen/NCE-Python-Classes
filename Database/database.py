#SQLite3
#CRUD: CREATE | READ | UPDATE | DELETE
import sqlite3

#Create database (if not exists)
conn = sqlite3.connect("mydb.db")
print("Database has created successfully!!")


#cursor (option)
cursor = conn.cursor()
#CREATE TABLES
cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,age INTEGER)""")
conn.commit()
print("Table created successfully!!")

#insert data
# cursor.execute("""INSERT INTO users(name,age) VALUES(?,?)""",("Alen",20))
# cursor.execute("""INSERT INTO users(name,age) VALUES(?,?)""",("Saniya",23))
# cursor.execute("""INSERT INTO users(name,age) VALUES(?,?)""",("Gulfam",23))
# conn.commit()
# print("data inserted succesfuly!")


#Read / Retrieve Data
cursor.execute("""SELECT * FROM users""")
rows = cursor.fetchall()#fetchone()
# print(rows)#tuple #[(1, 'Alen', 20), (2, 'Saniya', 23), (3, 'Gulfam', 23)]

for row in rows:
    print(row)
    # print(row[1])

cursor.execute("""SELECT * FROM users WHERE name=?""",("Gulfam",))
res = cursor.fetchone()
print(res)

#UPDATE Data
cursor.execute("""UPDATE users SET age=? WHERE name=?""",(40,"Alen"))
conn.commit()


#Delete Data
cursor.execute("""DELETE FROM users WHERE name=?""",("Alen",))
conn.commit()

#Delete Table
cursor.execute("""DROP TABLE users""")
conn.commit()
print("table deleted successfully!!")