#7. Dictionary keys and values — important rules
#Keys must be unique
data = {
    "name": "Akash",
    "name": "Alok"
}

print(data)
# {'name': 'Alok'}
#The second value replaces the first because the same key is assigned twice.
'''
Keys must be hashable
Strings, integers, and many tuples can be dictionary keys. Lists, sets, and dictionaries cannot be used directly as keys because they are unhashable.
'''
data = {
    "name": "Akash",
    10: "Ten",
    (1, 2): "Coordinate"
}

print(data["name"])
print(data[10])
print(data[(1, 2)])