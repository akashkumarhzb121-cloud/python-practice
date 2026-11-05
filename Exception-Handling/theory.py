#1. What is an exception?
'''
An exception is an error or unexpected condition that occurs during program execution and interrupts the normal flow of the program.

For example:
'''
a = 10
b = 0

print(a / b)

#Python cannot divide a number by zero, so it raises a ZeroDivisionError., Another example:
number = int("hello")
#This raises a ValueError because "hello" cannot be converted into an integer
'''
Common exceptions:
Exception	        When it occurs
ZeroDivisionError	Dividing by zero
ValueError	        Value has an inappropriate format
TypeError	        An operation receives an incompatible type
NameError       	A variable name is not defined
IndexError      	A sequence index is out of range
KeyError	        A dictionary key is missing
FileNotFoundError	A requested file cannot be found
ImportError     	An import fails
AttributeError	    An object doesn't have the requested attribute
'''
