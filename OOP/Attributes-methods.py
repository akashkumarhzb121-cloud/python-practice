#3. Attributes and methods
'''
A class usually contains two important things:
- Attributes: Data associated with an object.
- Methods: Functions defined inside a class that describe its behavior.
'''
class Student:
    def show_details(self):
        print(self.name, self.marks)

s1 = Student()
s1.name = "Akash"
s1.marks = 85

s1.show_details()
'''
Here, name and marks are attributes, while show_details() is a method.

This example creates attributes after the object is created. A more structured approach is to initialize them with __init__().
'''