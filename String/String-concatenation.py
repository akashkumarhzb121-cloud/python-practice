#5. String concatenation and repetition
#Concatenation (+)
# Joins strings together.
first = "Akash"
last = "Kumar"

full_name = first + " " + last
print(full_name)

#You cannot directly concatenate a string and an integer:
age = 20

# print("Age: " + age)  # TypeError
print("Age: " + str(age))  # Age: 20

#Repetition (*)
# Repeats a string a specified number of times.
print("Hi " * 3)