
from pathlib import Path
import csv
from datetime import datetime


base_dir = Path.cwd() / "pathlib_practise"

folders = [
    "university",
    "students",
    "teacchers",
    "courses",
    "reports"
]

for folder in folders:
    (base_dir / folder).mkdir(parents=True, exist_ok=True)

print("University directory created successfully!")


# =====================================
# 2. DEFINE CSV FILE PATHS
# =====================================

student_file = base_dir / "students" / "students.csv"
teacher_file = base_dir / "teacchers" / "teachers.csv"
course_file = base_dir / "courses" / "courses.csv"


# =====================================
# 3. CREATE CSV FILES WITH HEADERS
# =====================================

def create_csv(file_path, headers):

    if not file_path.exists():
        with file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

        print(f"{file_path.name} created!")


create_csv(
    student_file,
    ["ID", "Name", "Department", "Semester", "Email"]
)

create_csv(
    teacher_file,
    ["ID", "Name", "Department", "Specialization"]
)

create_csv(
    course_file,
    ["Course_ID", "Course_Name", "Credit_Hours", "Instructor"]
)


# =====================================
# 4. ADD STUDENT RECORDS
# =====================================

def add_student():

    print("\n--- Add New Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")
    email = input("Enter Email: ")

    student_data = [
        student_id,
        name,
        department,
        semester,
        email
    ]

    with student_file.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

    print("Student added successfully!")


# =====================================
# 5. ADD TEACHER RECORDS
# =====================================

def add_teacher():

    print("\n--- Add New Teacher ---")

    teacher_id = input("Enter Teacher ID: ")
    name = input("Enter Teacher Name: ")
    department = input("Enter Department: ")
    specialization = input("Enter Specialization: ")

    teacher_data = [
        teacher_id,
        name,
        department,
        specialization
    ]

    with teacher_file.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(teacher_data)

    print("Teacher added successfully!")


# =====================================
# 6. ADD COURSE RECORDS
# =====================================

def add_course():

    print("\n--- Add New Course ---")

    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    credit_hours = input("Enter Credit Hours: ")
    instructor = input("Enter Instructor Name: ")

    course_data = [
        course_id,
        course_name,
        credit_hours,
        instructor
    ]

    with course_file.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(course_data)

    print("Course added successfully!")


# =====================================
# 7. DISPLAY STUDENTS
# =====================================

def display_students():

    print("\n--- All Students ---")

    with student_file.open("r", newline="", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))


# =====================================
# 8. SEARCH FOR STUDENT
# =====================================

def search_student():

    search_id = input("\nEnter Student ID to search: ")

    found = False

    with student_file.open("r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for student in reader:

            if student["ID"] == search_id:

                print("\nStudent Found!")
                print(student)

                found = True
                break

    if not found:
        print("Student not found!")


# =====================================
# 9. GENERATE UNIVERSITY REPORT
# =====================================

def generate_report():

    report_file = base_dir / "reports" / "university_report.txt"

    with student_file.open("r", encoding="utf-8") as file:
        students = list(csv.DictReader(file))

    with teacher_file.open("r", encoding="utf-8") as file:
        teachers = list(csv.DictReader(file))

    with course_file.open("r", encoding="utf-8") as file:
        courses = list(csv.DictReader(file))

    report = f"""
UNIVERSITY MANAGEMENT REPORT
================================

Report Generated: {datetime.now()}

Total Students: {len(students)}
Total Teachers: {len(teachers)}
Total Courses: {len(courses)}

================================
END OF REPORT
"""

    report_file.write_text(report, encoding="utf-8")

    print("\nReport generated successfully!")
    print(report)


# =====================================
# 10. MAIN MENU
# =====================================

def main():

    while True:

        print("\n================================")
        print("     UNIVERSITY MANAGEMENT")
        print("================================")

        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Display Students")
        print("5. Search Student")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                add_teacher()

            elif choice == "3":
                add_course()

            elif choice == "4":
                display_students()

            elif choice == "5":
                search_student()

            elif choice == "6":
                generate_report()

            elif choice == "7":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice! Please try again.")

        except (OSError, csv.Error) as error:
            print(f"An error occurred: {error}")


# =====================================
# 11. RUN PROGRAM
# =====================================

if __name__ == "__main__":
    main()
