#1. What is a string in Python?
#A string (str) is a sequence of Unicode characters used to store text.

name = "Akash"
city = 'Jaipur'
message = "I am learning Python"

print(name)
print(type(name))  # <class 'str'>

#Strings can contain letters, digits, spaces, and symbols.
a = "Python"
b = "12345"
c = "Hello @2026!"

print(type(a))  # str
print(type(b))  # str
print(type(c))  # str

#Even though "12345" contains digits, it is a string because it is enclosed in quotes.
x = 12345
y = "12345"

print(type(x))  # int
print(type(y))  # str