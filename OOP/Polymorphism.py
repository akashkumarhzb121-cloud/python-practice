#D. Polymorphism and method overriding
#Method overriding occurs when a subclass provides its own implementation of an inherited method.
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

Dog().speak()
Cat().speak()
'''
The method name is the same, but the behavior differs.

Python also supports duck typing: code can work with different object types as long as they provide the methods or behavior it needs.
'''