#8. Nested dictionaries
#A nested dictionary is a dictionary stored inside another dictionary. It is useful when your data has multiple levels.
students = {
    "student1": {
        "name": "Akash",
        "marks": 85
    },
    "student2": {
        "name": "Rahul",
        "marks": 90
    }
}

print(students["student1"]["name"])   # Akash
print(students["student2"]["marks"])  # 90

#9. Dictionary comprehension
#Just as list comprehension creates lists, dictionary comprehension creates dictionaries in a concise way.
squares = {x: x**2 for x in range(1, 6)}

print(squares)
#The expression x: x**2 creates a key-value pair for every value of x.

#You can also filter entries:
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}

print(even_squares)
# {2: 4, 4: 16}