#1. What is Object-Oriented Programming?
'''
Object-Oriented Programming (OOP) is a programming approach in which we organize code around objects. An object combines data (attributes) and behavior (methods).
Think about a car:
A car has data such as its brand, color, and speed. It also has behaviors such as starting, accelerating, and braking.

In Python, we can represent these using a class and an object.
'''
class Car:
    def start(self):
        print("Car started")

my_car = Car()
my_car.start()
'''
Why use OOP?
- Organizes large programs into manageable parts.
- Makes code reusable.
- Keeps related data and behavior together.
- Helps represent real-world entities.
- Makes complex applications easier to maintain.
OOP is useful in applications such as banking systems, e-commerce platforms, student management systems, games, and data-processing software.
'''