class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.total = sum(marks)
        self.average = self.total / len(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B"
        elif self.average >= 60:
            return "C"
        elif self.average >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nStudent Details")
        print("---------------------------")
        print("Roll Number :", self.roll)
        print("Name        :", self.name)
        print("Marks       :", self.marks)
        print("Total       :", self.total)
        print("Average     :", round(self.average, 2))
        print("Grade       :", self.grade)


class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll = input("Enter Roll Number: ")

        if roll in self.students:
            print("Student already exists!")
            return

        name = input("Enter Student Name: ")

        marks = []
        for i in range(3):
            mark = float(input(f"Enter Marks of Subject {i+1}: "))
            marks.append(mark)

        student = Student(roll, name, marks)
        self.students[roll] = student

        print("Student record added successfully!")

    def search_student(self):
        roll = input("Enter Roll Number to Search: ")

        if roll in self.students:
            self.students[roll].display()
        else:
            print("Student not found!")

    def display_all(self):
        if not self.students:
            print("No student records available.")
            return

        print("\nAll Student Records")
        print("=" * 40)

        for student in self.students.values():
            student.display()


# Main Program
sms = StudentManagement()

while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.search_student()

    elif choice == "3":
        sms.display_all()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
