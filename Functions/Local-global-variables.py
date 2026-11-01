#7. Local and global variables
'''
Variable scope determines where a variable can be accessed.
Local variable
A variable created inside a function is generally local to that function.
'''
def show():
    message = "Hello Python"
    print(message)

show()
'''
This works because message is accessed inside its function.

Trying to access message outside the function will cause a NameError.
Global variable
A variable defined outside a function is generally available inside it.
'''
name = "Akash"

def show():
    print(name)

show()
#To reassign a global variable from inside a function, use global:
count = 0

def increase():
    global count
    count += 1

increase()
print(count)
#Use global sparingly. Often, returning the new value is clearer and easier to test