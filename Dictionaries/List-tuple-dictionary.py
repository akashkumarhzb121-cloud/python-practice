#11. List vs tuple vs dictionary
'''
Feature	    List	    Tuple	    Dictionary
Syntax	    []	        ()	        {key: value}
Access	    Index	    Index	    Key
Mutable	    Yes	        No	        Yes
Stores	    Items	    Items	    Key-value pairs
Best use	Changeable  sequences	Fixed sequences	Named data and lookups
'''
# List: access by position
marks = [80, 90, 85]
print(marks[0])  # 80

# Tuple: fixed sequence
point = (10, 20)
print(point[1])  # 20

# Dictionary: access by key
student = {"name": "Akash", "marks": 85}
print(student["marks"])  # 85