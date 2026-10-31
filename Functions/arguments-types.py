#5. Types of arguments in Python

#A. Positional arguments, Values are assigned according to their positions.
def student(name, age):
    print(name, age)

student("Akash", 20)
#Changing the order changes the assignments:
student(20, "Akash")

#B. Keyword arguments, Specify parameter names when calling the function.
def student(name, age):
    print(name, age)

student(age=20, name="Akash")
#Keyword arguments let you pass values in a different order.

#C. Default arguments, A parameter can have a default value, which is used when no argument is provided for it.
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Akash")

#Remember: Parameters with default values should generally come after parameters without default values.
def student(name, course="CSE"):
    print(name, course)

student("Akash")
student("Akash", "Data Science")

#D. Variable-length arguments: *args, Use *args when you want a function to accept any number of positional arguments
def add_all(*numbers):
    print(sum(numbers))

add_all(10, 20)
add_all(10, 20, 30, 40)
#Inside the function, numbers is a tuple.

#E. Variable-length keyword arguments: **kwargs, Use **kwargs when you want to accept any number of keyword arguments.
def details(**data):
    print(data)

details(name="Akash", age=20, course="CSE")
#Inside the function, data is a dictionary.
'''
Syntax	    Purpose	Collected               data
*args	    Multiple positional arguments	Tuple
**kwargs	Multiple keyword arguments	    Dictionary
'''