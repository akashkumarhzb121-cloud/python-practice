#3. The try and except blocks
'''
Python uses try and except to catch and handle exceptions.

Syntax:
try:
    # Code that might raise an exception
    statements
except ExceptionType:
    # What to do if that exception occurs
    statements
'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Program continues.")
'''
How it works:
1. Python starts executing the try block.
2. Division by zero raises ZeroDivisionError.
3. Python skips the remaining statements in that try block.
4. The matching except block runs.
5. Execution continues after the exception-handling structure.
'''