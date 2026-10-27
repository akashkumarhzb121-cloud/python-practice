#2. How to access dictionary values
#You can retrieve a value using its key inside square brackets.
student = {
    "name": "Akash",
    "age": 20,
    "branch": "CSE"
}

print(student["name"])    # Akash
print(student["age"])     # 20
print(student["branch"])  # CSE

#What happens if a key doesn't exist?
student = {"name": "Akash"}

# print(student["age"])  # KeyError
print(student.get("age"))  # None
print(student.get("age", 0))  # 0

'''
here are two important ways to access values:
- student["age"] raises a KeyError if the key doesn't exist.
- student.get("age", 0) returns the default value 0 if the key is absent.
Use square brackets when the key should exist. Use get() when a missing key is a normal possibility.
'''