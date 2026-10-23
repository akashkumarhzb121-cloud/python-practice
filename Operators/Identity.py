#7. Identity operators
'''
Identity operators check whether two references point to the same object, not merely whether their values are equal.
- is — same object.
- is not — different objects.
'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True
print(a is b)  # True
print(a is c)  # Falses
print(a is not c)  # True

'''
Why?
- a == c is True because the lists have equal contents.
- a is b is True because b refers to the same list as a.
- a is c is False because c is a separate list.
- a is not c is true because c is a separate list.
'''
#Use identity checks for None:
result = None

if result is None:
    print("No result available")
#Remember: Use == for value equality and is for object identity. Don't use is as a general replacement for ==.