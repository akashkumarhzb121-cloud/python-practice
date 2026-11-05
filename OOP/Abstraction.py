#B. Abstraction in more detail
#An abstract class defines an interface that concrete subclasses are expected to implement.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 3)
print(r.area())
'''
Output: 15

You cannot instantiate Shape directly while it has an unimplemented abstract method. Rectangle supplies the implementation.
'''