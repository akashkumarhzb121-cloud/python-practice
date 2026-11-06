#8. Raising exceptions with raise
'''
Sometimes Python does not automatically know that a value violates your application's rules. You can explicitly raise an exception.

Example: marks must be between 0 and 100.
'''
def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return marks

print(validate_marks(85))
validate_marks(150)
'''
raises a ValueError with the message "Marks must be between 0 and 100."

You can catch it at the point where you want to handle invalid marks:
'''
try:
    marks = validate_marks(150)
except ValueError as e:
    print(e)