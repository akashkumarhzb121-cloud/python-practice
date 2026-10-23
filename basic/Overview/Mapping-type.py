#4. Mapping type — Dictionary (dict)
'''
A dictionary stores information as key-value pairs.
Think of a student record: the key "name" maps to "Akash", while "marks" maps to 85.
'''
student = {
    "name": "Akash",
    "age": 20,
    "marks": 85
}

print(student["name"])   # Akash
print(student["marks"])  # 85

#Adding, updating, and deleting
student["city"] = "Jaipur"   # Add
student["marks"] = 90         # Update
del student["age"]            # Delete

print(student)

'''
Useful      dictionary methods:
Method	    Purpose
keys()	    Get the keys
values()	Get the values
items()	    Get key-value pairs
get(key)	Get a value safely if the key exists
update()	Add or update multiple pairs
pop(key)	Remove a key and return its value
'''
student = {"name": "Akash", "marks": 85}

print(student.get("age", 0))  # 0
print(list(student.keys()))   # ['name', 'marks']
print(list(student.values())) # ['Akash', 85]

'''
Unlike student["age"], student.get("age", 0) does not raise a KeyError when "age" is absent; it returns the supplied default.

Important properties:
- Dictionary keys must be unique and hashable.
- Values can be duplicated and can have different types.
- Dictionaries preserve insertion order in modern Python.
- Dictionaries are mutable.
'''