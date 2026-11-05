#10. Practical OOP project: Student Management System
class Student:
    college = "GIT Jaipur"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        return "D"

    def display(self):
        print(f"Name: {self.name}")
        print(f"College: {self.college}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

student1 = Student("Akash", 85)
student1.display()
'''
This example uses:
- A class and an object.
- A constructor to initialize data.
- Instance and class attributes.
- Instance methods.
- A returned result.
- Conditional logic.
In a larger student management application, you might add methods to update marks, validate input, calculate attendance, and save records to a database.
'''