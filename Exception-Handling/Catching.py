#7. Catching the exception message
'''
Sometimes you want to display the exception's message for debugging or logging.

Use as to bind the exception object to a variable.
'''
try:
    number = int("abc")
except ValueError as e:
    print("Conversion failed:", e)
'''
In a user-facing application, prefer a friendly message for users and keep technical details in logs when appropriate. Avoid exposing sensitive internal information.
Output will contain a message similar to:
Conversion failed: invalid literal for int() with base 10: 'abc'
'''