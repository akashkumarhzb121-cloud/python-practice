#5. Important dictionary methods
student = {
    "name": "Akash",
    "age": 20,
    "marks": 85
}

print(student.keys())
print(student.values())
print(student.items())

'''
Method	    What it returns
keys()	    A view of all keys
values()	A view of all values
items()	    A view of key-value pairs
get(key)	A value or None if missing
update()	Adds or updates entries
copy()	    A shallow copy
clear()	    Removes all entries

These views reflect changes to the dictionary. You can convert them to lists if you need a list snapshot:
'''
print(list(student.keys()))
# ['name', 'age', 'marks']