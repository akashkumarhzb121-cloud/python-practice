#6. Python is dynamically typed
'''
In languages such as C or Java, you commonly declare a variable's type explicitly. Python determines the type from the object assigned to a name.
The name x can refer to objects of different types at different times. Python does not permanently lock the name to int.
This is called dynamic typing.
'''
x = 100
print(type(x))    # int

x = "Python"
print(type(x))    # str

x = 3.14
print(type(x))    # float

#Dynamic typing does not mean every operation is allowed
age = 20
name = "Akash"
# print(age + name)  # TypeError

print(str(age) + name)  # 20Akash
print(age + 5)          # 25

#Use str() when converting a number to text, or use an f-string for readable output:
print(f"{name} is {age} years old.")