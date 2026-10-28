#6. Looping through a dictionary
#A for loop iterates over dictionary keys by default.
student = {
    "name": "Akash",
    "age": 20,
    "marks": 85
}

for key in student:
    print(key)

#To print both keys and values, use items():
for key, value in student.items():
    print(key, ":", value)

#To loop through only values:
for value in student.values():
    print(value)

    