#9. Recursive functions
'''
A recursive function calls itself to solve a smaller version of the same problem.

Example: factorial of a number.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
'''
How it works:
- factorial(5) calculates 5 * factorial(4).
- The calls continue until factorial(1) returns 1.
- The results multiply back up to produce 120.
Important: Every recursive function needs a base case; otherwise, it may keep calling itself until Python raises a RecursionError.
'''