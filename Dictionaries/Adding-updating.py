#3. Adding and updating dictionary items
#Dictionaries are mutable, which means you can add new key-value pairs or change existing values.
student = {
    "name": "Akash",
    "marks": 80
}

# Add a new key
student["city"] = "Jaipur"

# Update an existing value
student["marks"] = 95

print(student)

# Notice that assigning to an existing key updates its value; it doesn't create a duplicate key.

# You can also update multiple values using update():
student.update({
    "marks": 90,
    "age": 20
})

print(student)