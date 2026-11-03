#4. The __init__() method and self
#The __init__() method initializes an object's attributes when it is created.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

s1 = Student("Akash", 85)
s2 = Student("Rahul", 92)

s1.show_details()
s2.show_details()
'''
Understand these three things carefully:
- __init__() is automatically called when an instance is initialized.
- self refers to the current instance. It lets a method access that instance's attributes and other methods.
- self.name = name stores the argument in the object's name attribute.
Technically, __init__() is an initializer, not the method that creates the object itself.

How self works
When you write:
'''
s1.show_details()
'''
Python passes s1 as the first argument to the instance method. This is why the method definition includes self.

You don't normally pass self manually when calling the method.
'''