#2. How to define a function
'''
Python uses the def keyword to define a function.

Syntax:
def function_name(parameters):
    # function body
    statements
'''
def greet():
    print("Hello, welcome to Python!")

greet()
'''
Understand each part:
- def — tells Python you are defining a function.
- greet — the function's name.
- () — holds parameters, if any.
- : — starts the function body.
- Indented statements — the code that runs when the function is called.
- greet() — calls or executes the function.
'''
#Important: Defining a function does not execute its body. You must call it.
def greet():
    print("Hello")

print("Start")
greet()
print("End")