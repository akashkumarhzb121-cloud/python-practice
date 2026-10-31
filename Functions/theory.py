#1. Why do we need functions?
'''
Suppose you want to add two numbers three times.

Benefits of functions:
- Reuse code instead of repeating it.
- Make programs easier to read and maintain.
- Break large problems into smaller tasks.
- Test and debug individual parts more easily.
'''
#Without a function:
a = 10
b = 20
print(a + b)

a = 15
b = 25
print(a + b)

a = 30
b = 40
print(a + b)

#With a function:
def add(a, b):
    print(a + b)

add(10, 20)
add(15, 25)
add(30, 40)