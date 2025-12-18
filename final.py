#Programers: Devin Goshaw, and Mark Nyagaka
#Date:12/15-18/2025
#Program: Final (student data base)

import sqlite3

def main():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    add_students_table(cur)
    add_sample_students(cur)
    conn.commit()

    while True:
        print("\n1. Display table")
        print("2. Edit a student")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            display_students(cur)
        elif choice == '2':
            display_students(cur)  
            edit_student(cur, conn)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Please choose one of the options")

    conn.close()


def add_students_table(cur):
    cur.execute('DROP TABLE IF EXISTS Students')
    cur.execute('''
        CREATE TABLE Students(
            StudentID INTEGER PRIMARY KEY NOT NULL,
            FirstName TEXT,
            LastName TEXT,
            Major TEXT,
            GPA REAL,
            CreditsCompleted INTEGER,
            Email TEXT,
            Standing TEXT,
            IsFullTime INTEGER,
            GradYear INTEGER
        )
    ''')


def add_sample_students(cur):
    students = [
        (1, 'Alex', 'Johnson', 'Computer Science', 3.6, 45, 'alex.johnson@example.edu', 'Sophomore', 1, 2027),
        (2, 'Bob', 'Lopez', 'Nursing', 3.9, 75, 'maria.lopez@example.edu', 'Junior', 1, 2026),
        (3, 'Fred', 'Carter', 'Business', 2.8, 30, 'jamal.carter@example.edu', 'Freshman', 1, 2028),
        (4, 'Joe', 'Nguyen', 'Psychology', 3.4, 90, 'sofia.nguyen@example.edu', 'Senior', 1, 2025),
        (5, 'Ethan', 'Kim', 'Engineering', 3.1, 60, 'ethan.kim@example.edu', 'Junior', 0, 2026),
        (6, 'Layla', 'Patel', 'Art', 3.7, 18, 'layla.patel@example.edu', 'Freshman', 0, 2029),
        (7, 'Noah', 'Williams', 'Cybersecurity', 2.9, 33, 'noah.williams@example.edu', 'Sophomore', 0, 2027)
    ]

    cur.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', students)


def display_students(cur):
    cur.execute('SELECT * FROM Students')
    rows = cur.fetchall()

    print("\nID | First Name | Last Name | Major               | GPA  | Credits | Email                        | Standing   | Full-Time | Grad Year")
    print("-" * 130)

    for row in rows:
        fulltime = "Yes" if row[8] == 1 else "No"
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<10} | {row[3]:<18} | {row[4]:<4.2f} | {row[5]:<7} | {row[6]:<28} | {row[7]:<10} | {fulltime:<9} | {row[9]}")


def edit_student(cur, conn):
    student_id = input("Enter the Student ID to edit: ")

    cur.execute('SELECT * FROM Students WHERE StudentID = ?', (student_id,))
    student = cur.fetchone()

    if not student:
        print("Student not found.")
        return

    print("\nPress Enter to keep the current value\n")

    first = input(f"First Name [{student[1]}]: ") or student[1]
    last = input(f"Last Name [{student[2]}]: ") or student[2]
    major = input(f"Major [{student[3]}]: ") or student[3]
    gpa = input(f"GPA [{student[4]}]: ") or student[4]
    credits = input(f"Credits Completed [{student[5]}]: ") or student[5]
    email = input(f"Email [{student[6]}]: ") or student[6]
    standing = input(f"Standing [{student[7]}]: ") or student[7]
    fulltime = input(f"Full Time (1=yes, 0=no) [{student[8]}]: ") or student[8]
    grad_year = input(f"Graduation Year [{student[9]}]: ") or student[9]

    cur.execute('''
        UPDATE Students
        SET FirstName=?, LastName=?, Major=?, GPA=?, CreditsCompleted=?,
            Email=?, Standing=?, IsFullTime=?, GradYear=?
        WHERE StudentID=?
    ''', (first, last, major, gpa, credits, email, standing, fulltime, grad_year, student_id))

    conn.commit()
    print("Student record updated successfully.")


if __name__ == '__main__':
    main()
