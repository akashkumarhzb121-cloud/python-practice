#1. What is a dictionary?
'''
A dictionary is a mutable collection that stores data as key-value pairs.

Think of a student record:
- Key: "name" → Value: "Akash"
- Key: "age" → Value: 20
- Key: "marks" → Value: 85
Instead of remembering that the name is at index 0 and the age is at index 1, you access the values using meaningful keys.
'''
student = {
    "name": "Akash",
    "age": 20,
    "marks": 85
}

print(student)
print(type(student))

'''
Dictionary syntax
my_dict = {
    key1: value1,
    key2: value2
}
A key identifies the value.
A value is the data associated with that key.
Keys must be unique and hashable.
Values can be duplicated and can have different data types.
Dictionaries preserve insertion order in modern Python.
'''
