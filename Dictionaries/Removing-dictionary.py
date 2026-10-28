#4. Removing dictionary items
'''
Python provides several methods for removing items.
Method	    Purpose
pop(key)	Removes a key and returns its value
popitem()	Removes and returns the last inserted key-value pair
del	        Deletes a specified key
clear()	    Removes all items
'''
student = {
    "name": "Akash",
    "age": 20,
    "marks": 85
}

student.pop("age")
del student["marks"]

print(student)
# {'name': 'Akash'}

#Using pop() with a default prevents an error if the key is missing:
student = {"name": "Akash"}

age = student.pop("age", None)
print(age)  # None