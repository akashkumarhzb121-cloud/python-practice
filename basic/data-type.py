#4. What are data types?
#A data type tells Python what kind of value an object represents and what operations can be performed on it.

age = 20
price = 99.5
name = "Akash"
is_student = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_student))

#The type() function tells us the type of an object.

#Why do data types matter?
# a = 10
# b = 20

# print(a + b)   # 30

a = "10"
b = "20"

print(a + b)   # 1020

#The first example adds two integers. The second joins two strings together, an operation called concatenation.

#5. The main Python data types


'''
Integer (int)
Whole numbers without a decimal point.
Python integers can grow beyond the fixed-size integer limits common in many other languages, subject to available memory.
'''
x = 25
y = -10
z = 0
print(type(x))  # int

'''
Float (float)
Numbers with a decimal or fractional part.
Note: floats use binary floating-point representation, so some decimal calculations are not perfectly exact.
'''
price = 99.50
temperature = -2.5
print(type(price))  # float

'''
String (str)
Text enclosed in single, double, or triple quotes.
Python has no separate char type. Even a single character is a string.
'''
name2 = "Akash"
letter = 'A'
message = """Hello Python"""
print(type(name2))  # str

'''
Boolean (bool)
Represents logical truth values: True or False.
Capitalization matters: write True and False, not true or false.
'''
is_passed = True
is_absent = False
print(type(is_passed))  # bool

'''
None (NoneType)
Represents the absence of a value.
It is different from 0, False, and an empty string.
'''
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>