#9. Short-hand conditional expression
'''
Python allows a simple conditional expression in one line.

Its general structure is:
value_if_true if condition else value_if_false

Use it for simple choices. For multiple branches or complex logic, regular if-elif-else statements are easier to read.
'''
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)