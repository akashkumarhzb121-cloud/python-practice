#1. What is a variable?
name = "Akash"
age = 20
marks = 85.5
passed = True

print(name)
print(age)
print(marks)
print(passed)

'''
name is an identifier — the name used to refer to a value.

= is the assignment operator, not a mathematical equality test.

"Akash" is a string value.

print(name) retrieves the value associated with the name and displays it.
'''

#2. How assignment works
'''
x = 10
x = 20

print(x) #20
'''

x = 10
y = x
x = 50

print(x)  # 50
print(y)  # 10

'''
y received the value referenced by x at the time of assignment. Reassigning x later does not automatically reassign y
'''

#3. Rules for naming variables
student_name = "Akash"   # Valid
age2 = 20                 # Valid
_total = 500              # Valid

print(student_name, age2, _total)

# 2age = 20       # Cannot start with a digit
# student-name   # Hyphen is not allowed
# class = "CSE"   # 'class' is a reserved keyword

"""
Important naming rules
1. A name can contain letters, digits, and underscores.
2. A name cannot start with a digit.
3. Names are case-sensitive: age, Age, and AGE are different.
4. Python keywords such as if, for, class, and True cannot be used as ordinary variable names.
5. Use descriptive names such as student_marks instead of unclear names such as sm.
"""
#To see Python's reserved keywords:
import keyword
print(keyword.kwlist)


