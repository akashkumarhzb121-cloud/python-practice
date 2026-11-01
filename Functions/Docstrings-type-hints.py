#10. Docstrings and type hints
'''
Docstrings
A docstring describes what a function does.
'''
def square(n):
    """Return the square of a number."""
    return n * n

print(square.__doc__)

#Type hints, Type hints indicate the expected input and output types.
def add(a: int, b: int) -> int:
    return a + b
'''
Here, a and b are expected to be integers, and the return value is indicated as an integer.

Type hints improve readability, but Python does not automatically enforce them at runtime.
'''

#11. Practical Data Science example- Imagine calculating a student's percentage from five subject marks.
def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

marks = [80, 75, 90, 85, 70]

result = calculate_percentage(marks)

print("Percentage:", result, "%")