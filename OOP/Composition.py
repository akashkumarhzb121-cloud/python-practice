#9. Composition: building objects from other objects
'''
Inheritance represents an is-a relationship. Composition represents a has-a relationship.

For example, a car has an engine.
'''
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready")

car = Car()
car.start()
#Composition is often a good choice when you want to combine separate components without forcing them into an inheritance hierarchy.