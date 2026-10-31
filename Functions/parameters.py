#3. Functions with parameters

def greet(name):
    print("Hello", name)

greet("Akash")
greet("Rahul")
'''
A parameter is a variable written inside the function definition. It receives a value when the function is called.

Here, name is the parameter, while "Akash" and "Rahul" are arguments.
- Parameter: variable in the function definition.
- Argument: actual value passed during the function call.
'''
#Function with multiple parameters
def add(a, b):
    print(a + b)

add(10, 20)