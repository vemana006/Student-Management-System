# Student Record Management System

students = {}

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter Marks of Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    print("Student record added successfully!")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        s = students[roll]

        print("\nStudent Details")
        print("----------------------")
        print("Roll Number :", roll)
        print("Name        :", s["Name"])
        print("Marks       :", s["Marks"])
        print("Total       :", s["Total"])
        print("Average     :", round(s["Average"], 2))
        print("Grade       :", s["Grade"])
    else:
        print("Student not found!")

def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nAll Student Records")
    print("-" * 60)

    for roll, s in students.items():
        print("Roll Number :", roll)
        print("Name        :", s["Name"])
        print("Marks       :", s["Marks"])
        print("Total       :", s["Total"])
        print("Average     :", round(s["Average"], 2))
        print("Grade       :", s["Grade"])
        print("-" * 60)

# Main Menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student Record")
    print("2. Search Student Details")
    print("3. Display All Student Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        display_students()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
