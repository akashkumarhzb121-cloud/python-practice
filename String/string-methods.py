#6. Important string methods
'''
A string method is a built-in operation you call on a string using dot notation.

General syntax:
string.method()

A. Case conversion methods
Method	        Purpose	                                                    Example              result
upper()     	Convert to uppercase	                                "hello".upper() →       "HELLO"
lower()	        Convert to lowercase	                                "HELLO".lower() →       "hello"
title()	        Capitalize words	                                    "hello world".title() → "Hello World"
capitalize()	Capitalize the first character and lowercase the rest	"hELLO".capitalize() →  "Hello"
swapcase()	    Swap letter case	                                    "PyThOn".swapcase() →   "pYtHoN"
casefold()	    Normalize text for caseless comparison	                "HELLO".casefold() →    "hello"
'''
text = "python programming"

print(text.upper())
print(text.capitalize())
print(text.title())


'''
B. Removing spaces and characters
Method	    Purpose
strip()	    Remove whitespace from both ends
lstrip()	Remove whitespace from the left
rstrip()	Remove whitespace from the right
'''
text = "   Hello Python   "

print(text.strip())   # Hello Python
print(text.lstrip())  # Hello Python   
print(text.rstrip())  #    Hello Python

#You can also provide characters to remove:
text = "***Python***"
print(text.strip("*"))  # Python
#Note: strip("*") removes matching * characters from the ends, not from the middle.

'''
C. Searching within strings
Method	        Purpose
find()	        Returns the first matching index, or -1 if absent
rfind()	        Finds the last matching index, or -1 if absent
index()	        Like find(), but raises ValueError if absent
count()	        Counts non-overlapping occurrences
startswith()	Checks the beginning
endswith()	    Checks the ending
'''
text = "Python Programming"

print(text.find("Pro"))        # 7
print(text.find("Java"))       # -1
print(text.count("m"))         # 2
print(text.startswith("Py"))   # True
print(text.endswith("ing"))    # True

#Difference between find() and index():
text = "Python"

print(text.find("z"))  # -1
# print(text.index("z"))  # ValueError

'''
D. Replacing text
replace(old, new) returns a string with matching occurrences replaced.
'''
text = "I like Java"
new_text = text.replace("Java", "Python")

print(new_text)  # I like Python
print(text)      # I like Java

#You can limit the number of replacements:
text = "apple apple apple"
print(text.replace("apple", "mango", 1))

'''
E. Splitting and joining
These methods are important for processing text and data.

split() — string to list
'''
text = "Python,Java,C++"
languages = text.split(",")

print(languages)
# ['Python', 'Java', 'C++']

#By default, split() separates on whitespace.
text = "Learn Python daily"
print(text.split())
# ['Learn', 'Python', 'daily']

#join() — iterable of strings to string
words = ["Learn", "Python", "daily"]

result = " ".join(words)
print(result)

#The string before .join() becomes the separator.
print("-".join(["2026", "10", "25"]))
# 2026-10-25
#join() expects string elements; it does not automatically convert integers into strings.

'''
F. Checking string contents
These methods return True or False.
Method	    Checks whether the string contains
isalpha()	Letters only
isdigit()	Digit characters
isalnum()	Letters or digits only
isspace()	Whitespace only
islower()	Cased letters are lowercase
isupper()	Cased letters are uppercase
istitle()	Title-case formatting
'''
print("Python".isalpha())  # True
print("12345".isdigit())   # True
print("Python123".isalnum())  # True
print("   ".isspace())     # True
print("hello".islower())   # True
print("HELLO".isupper())   # True

#A space makes isalpha() false:
print("Hello World".isalpha())  # False

'''
G. Formatting strings
F-strings are a convenient way to insert variables into text.
'''
name = "Akash"
age = 20

print(f"My name is {name} and I am {age} years old.")

#You can format numbers, too:
price = 45.6789

print(f"{price:.2f}")  # 45.68
#The .2f format displays two digits after the decimal point.