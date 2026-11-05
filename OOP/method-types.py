#7. Types of methods in Python
'''
Python classes commonly use three kinds of methods.
Instance method
Works with an individual object's data and uses self.
'''
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

#Class method, Uses @classmethod and receives the class as cls.
class Student:
    college = "GIT Jaipur"

    @classmethod
    def change_college(cls, name):
        cls.college = name

Student.change_college("New College")
print(Student.college)

#Static method, Uses @staticmethod when the operation logically belongs to the class but doesn't need the instance or class as an implicit first argument.
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

#8. Special methods and operator overloading
'''
Special methods, often called dunder methods, have names with double underscores, such as __init__ and __str__.

You can use them to define how your objects interact with built-in Python operations.
'''
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

book = Book("Python Basics")
print(book)
'''
Without __str__(), printing a custom object usually produces a less readable representation.

You can also define methods such as __add__() to customize the + operator for your own class. This is known as operator overloading.
'''