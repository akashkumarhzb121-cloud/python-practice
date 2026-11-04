#6. The four pillars of OOP
#The four commonly taught pillars are encapsulation, abstraction, inheritance, and polymorphism.
'''
1. Encapsulation

Combining data and related methods in a class, while controlling how the data is accessed or modified.
__balance uses Python's name-mangling convention. It discourages direct access; it is not absolute privacy.
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

'''
2. Abstraction

Exposing the essential operations while hiding unnecessary implementation details.

For example, you press a car's start button without needing to understand the entire engine-control system.
A concrete payment class must implement pay() to be instantiated.
'''
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

'''
3. Inheritance

Creating a new class from an existing class so that it can reuse or extend its behavior.
Output: Animal sound
'''
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

Dog().speak()

'''
4. Polymorphism

The same method interface can produce different behavior for different object types.
Output: Bark, then Meow.
'''
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()