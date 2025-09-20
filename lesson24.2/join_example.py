import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXIST courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        student_id ITEGER,
        FOREIGN KEY(student_id) REFERENCE students(student_id)
        )
    
''')

cursor.execute("INSERT INTO students (name) VALUES ('ALICE')")
cursor.execute("INSERT INTO students (name) VALUES ('Bob')")

cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Math',1)")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Science',1)")
cursor.execute("INSERT INTO courses ( course_name, student_id) VALUES ('Art',2)")

conn.commit()

cursor.execute('''
    SELECT students.name, courses.course_name from students
    JOIN courses on students.student_id = courses.student_id
    
''')

rows = cursor.fetchall()

for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

conn.close()