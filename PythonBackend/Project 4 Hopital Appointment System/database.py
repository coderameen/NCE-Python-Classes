import sqlite3

#connections
conn = sqlite3.connect("hospitaldb.db", check_same_thread = False)
print("db created success")
cursor = conn.cursor()

#table -doctor
cursor.execute("""CREATE TABLE IF NOT EXISTS doctors(d_id INTEGER PRIMARY KEY AUTOINCREMENT,d_name TEXT,d_specialization TEXT,d_status TEXT,d_comment TEXT)""")
#table - patient
cursor.execute("""CREATE TABLE IF NOT EXISTS patients(p_id INTEGER PRIMARY KEY,p_name TEXT, p_time TEXT,d_name TEXT)""")


conn.commit()

# print("table created success")

# #inset doctor
# cursor.execute("""INSERT INTO doctors(d_name,d_specialization,d_status,d_comment) VALUES(?,?,?,?)""",("dr_alen","neurologist","available","I will be available from 6PM to 8PM"))
# cursor.execute("""INSERT INTO doctors(d_name,d_specialization,d_status,d_comment) VALUES(?,?,?,?)""",("dr_bob","orthopedic surgeon","unavailable","I will be on leave!"))
# cursor.execute("""INSERT INTO doctors(d_name,d_specialization,d_status,d_comment) VALUES(?,?,?,?)""",("dr_kelvin","cardiologist","available","I will be avaialble from 8PM to 10PM"))
# conn.commit()
# print("doctors added successfuly!")

# #insert patient
# cursor.execute("""INSERT INTO patients(p_name,p_time,d_name) VALUES(?,?,?)""",("Gyan","22/2/2025 21:00","dr_bob"))
# conn.commit()
# print("patient added successfully")