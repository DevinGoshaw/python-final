import sqlite3

def main():
    conn = sqlite3.connect('students.db')

    cur = conn.cursor()

    add_students_table(cur)

    add_sample_students(cur)

    conn.commit()

    display_students(cur)

    conn.close()
    print("\nstudents.db created and populated successfully.")

def add_students_table(cur):
    """Create the Students table (drop first if it exists)."""
    cur.execute('DROP TABLE IF EXISTS Students')

    cur.execute('''
        CREATE TABLE Students (
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
    """Insert sample rows for testing."""
    students = [
        (1, 'Alex',    'Johnson',  'Computer Science', 3.6,  45, 'alex.johnson@example.edu',  'Sophomore', 1, 2027),
        (2, 'Maria',   'Lopez',    'Nursing',          3.9,  75, 'maria.lopez@example.edu',   'Junior',    1, 2026),
        (3, 'Jamal',   'Carter',   'Business',         2.8,  30, 'jamal.carter@example.edu',  'Freshman',  1, 2028),
        (4, 'Sofia',   'Nguyen',   'Psychology',       3.4,  90, 'sofia.nguyen@example.edu',  'Senior',    1, 2025),
        (5, 'Ethan',   'Kim',      'Engineering',      3.1,  60, 'ethan.kim@example.edu',     'Junior',    1, 2026),
        (6, 'Layla',   'Patel',    'Art',              3.7,  18, 'layla.patel@example.edu',   'Freshman',  0, 2029),
        (7, 'Noah',    'Williams', 'Cybersecurity',    2.9,  33, 'noah.williams@example.edu', 'Sophomore', 1, 2027),
        (8, 'Grace',   'Miller',   'Biology',          3.5, 105, 'grace.miller@example.edu',  'Senior',    1, 2025),
        (9, 'Omar',    'Ali',      'Data Science',     3.2,  48, 'omar.ali@example.edu',      'Sophomore', 1, 2027),
        (10,'Faith',   'Brown',    'Theology',         3.8,  72, 'faith.brown@example.edu',   'Junior',    1, 2026)
    ]

    for row in students:
        cur.execute('''
            INSERT INTO Students
            (StudentID, FirstName, LastName, Major, GPA,
             CreditsCompleted, Email, Standing, IsFullTime, GradYear)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

def display_students(cur):
    """Print all students in a nice format."""
    print("Contents of students.db / Students table:\n")
    cur.execute('SELECT StudentID, FirstName, LastName, Major, GPA, Standing, GradYear FROM Students')
    results = cur.fetchall()

    print(f"{'ID':<3} {'Name':25} {'Major':20} {'GPA':<4} {'Standing':10} {'GradYear'}")
    print("-" * 80)
    for row in results:
        student_id = row[0]
        full_name = f"{row[1]} {row[2]}"
        major = row[3]
        gpa = row[4]
        standing = row[5]
        grad_year = row[6]
        print(f"{student_id:<3} {full_name:25} {major:20} {gpa:<4.2f} {standing:10} {grad_year}")

if __name__ == '__main__':
    main()