#8. Lambda functions
'''
A lambda function is a small anonymous function written in one expression.

Syntax:
lambda arguments: expression
'''
square = lambda x: x * x

print(square(5))
#Equivalent regular function:
def square(x):
    return x * x
#Lambda functions are especially useful for short operations, such as sorting.
students = [("Aman", 75), ("Riya", 90), ("Akash", 85)]

students.sort(key=lambda student: student[1])

print(students)
#This sorts students by marks in ascending order.