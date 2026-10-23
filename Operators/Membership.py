#6. Membership operators
'''
Membership operators check whether an element exists inside a collection or sequence.
- in — checks whether an element is present.
- not in — checks whether an element is absent.
'''
fruits = ["apple", "mango", "banana"]

print("mango" in fruits)       # True
print("orange" not in fruits)  # True

#Membership works with strings, too:
text = "Python Programming"

print("Python" in text)  # True
print("Java" in text)    # False

#Dictionary reminder: Membership tests keys, not values, by default.
student = {"name": "Akash", "marks": 85}

print("name" in student)    # True
print("Akash" in student)   # False
print("Akash" in student.values())  # True