#C. Inheritance in more detail
#Python supports single, multiple, multilevel, and hierarchical inheritance.
class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()
s.introduce()
s.study()
#The Student class reuses introduce() from Person and defines its own study() method.