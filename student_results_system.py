"""
Digital Exam & Results Management System
Domain: Education
Covers: OOP (Task 1), one data structure (Task 2), instance + class methods (Task 3)
Privacy: only a student ID, name and scores are stored. No sensitive personal data.
"""


# ---------------------------------------------------------------
# TASK 1: Classes, attributes, methods, object interaction
# ---------------------------------------------------------------
class Result:
    """A single subject result."""

    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def display_info(self):
        return f"{self.subject}: {self.score}"


class Student:
    """A student who holds Result objects."""

    total_students = 0  # class attribute shared by all students

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.results = {}  # subject -> Result object
        Student.total_students += 1

    # ----- Instance methods (Task 3) -----
    def add_result(self, result):
        """Interaction: a Student object stores a Result object."""
        self.results[result.subject] = result

    def update_record(self, name):
        self.name = name

    def average(self):
        if not self.results:
            return 0
        scores = [r.score for r in self.results.values()]
        return sum(scores) / len(scores)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        return "F"

    def display_info(self):
        print(f"\nID: {self.student_id} | Name: {self.name}")
        if not self.results:
            print("  No results recorded yet.")
        for r in self.results.values():
            print(f"  - {r.display_info()}")
        print(f"  Average: {self.average():.1f} | Grade: {self.grade()}")

    # ----- Class methods (Task 3) -----
    @classmethod
    def from_string(cls, text):
        """Create a Student from 'ID,Name' text."""
        student_id, name = text.split(",")
        return cls(student_id.strip(), name.strip())

    @classmethod
    def get_total_students(cls):
        return cls.total_students


# ---------------------------------------------------------------
# TASK 2: ONE data structure - a dictionary keyed by student ID
# ---------------------------------------------------------------
students = {}


def add_student(student):
    if student.student_id in students:
        print("A student with that ID already exists.")
        return False
    students[student.student_id] = student
    return True


def display_students():
    if not students:
        print("\nNo students recorded yet.")
        return
    for student in students.values():
        student.display_info()
    print(f"\nTotal students: {Student.get_total_students()}")


# ---------------------------------------------------------------
# Menu program
# ---------------------------------------------------------------
def load_sample_data():
    samples = ["S001, Aminata Kamara", "S002, Mohamed Sesay", "S003, Fatmata Bangura"]
    scores = {
        "S001": [("Maths", 85), ("English", 78), ("Science", 90)],
        "S002": [("Maths", 62), ("English", 70), ("Science", 55)],
        "S003": [("Maths", 45), ("English", 52), ("Science", 40)],
    }
    for text in samples:
        student = Student.from_string(text)
        if add_student(student):
            for subject, score in scores[student.student_id]:
                student.add_result(Result(subject, score))
    print("Sample data loaded.")


def read_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    while True:
        print("\n=== Digital Exam & Results Management System ===")
        print("1. Add student")
        print("2. Add result for a student")
        print("3. Display all students")
        print("4. Update student name")
        print("5. Load sample data")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            if student_id and name and add_student(Student(student_id, name)):
                print("Student added.")
        elif choice == "2":
            student = students.get(input("Student ID: ").strip())
            if student:
                subject = input("Subject: ").strip()
                student.add_result(Result(subject, read_score("Score (0-100): ")))
                print("Result added.")
            else:
                print("Student not found.")
        elif choice == "3":
            display_students()
        elif choice == "4":
            student = students.get(input("Student ID: ").strip())
            if student:
                student.update_record(input("New name: ").strip())
                print("Record updated.")
            else:
                print("Student not found.")
        elif choice == "5":
            load_sample_data()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
