#4. The return statement
'''

This is one of the most important concepts in functions.

The return statement sends a result back to the place where the function was called.
'''
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

#Difference between print() and return
def add1(a, b):
    print(a + b)

def add2(a, b):
    return a + b

x = add1(10, 20)
y = add2(20, 30)

print("x =", x)
print("y =", y)
'''
Why?
- print() displays a value but does not send that value back as the function's result.
- return sends the result back so it can be stored, reused, or calculated with.
- If a function finishes without an explicit return, Python returns None.
For real programs, use return when you need to reuse the calculated result.
'''
def square(n):
    return n * n

answer = square(5)
print(answer + 10)