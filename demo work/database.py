import sqlite3
conn = sqlite3.connect("hospitaldb.db",check_same_thread=False)
print("db created successfully!")

cursor = conn.cursor()
#patient table
cursor.execute("""CREATE TABLE IF NOT EXISTS(patient_id TEXT PRIMARY KEY,name TEXT not NULL,appoinment_time TEXT,doctor_id TEXT,doctor_name TEXT,status TEXT""")
print("patient table created successfully!")

cursor.execute("""CREATE TABLE IF NOT EXISTS(doctor_id TEXT PRIMARY KEY,doctor_name TEXT,patient_id TEXT,patient_name TEXT,status TEXT""")
print("doctor table created successfully")