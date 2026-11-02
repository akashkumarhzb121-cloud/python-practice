#2. Classes and objects
'''
These are the foundation of OOP.

Class: A blueprint describing what an object will contain and what it can do.

Object: A specific instance created from a class.

For example, Student can be a class, while Akash and Rahul can be two different student objects.
'''
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))
print(type(s2))
'''
Both s1 and s2 are separate objects created from the Student class. pass simply means that the class body is currently empty.

Remember:
- class defines a class.
- s1 = Student() creates an object.
- s1 is a variable referring to that object.
'''