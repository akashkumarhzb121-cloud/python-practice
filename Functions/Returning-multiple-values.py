#6. Returning multiple values
#Python can return multiple values from a function. They are packaged into a tuple.
def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)
#This is called multiple assignment or unpacking of the returned tuple.