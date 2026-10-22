#2. Sequence types
'''
A. String (str)
A string is an immutable sequence of Unicode characters.
'''
text = "PYTHON"

print(text[0])     # P
print(text[-1])    # N
print(text[1:4])   # YTH
print(len(text))   # 6

#Useful string operations:
name = "  akash kumar  "

print(name.upper())           #   AKASH KUMAR
print(name.strip())           # akash kumar
print(name.title())           # Akash Kumar
print(name.replace("akash", "Alok"))
print("Python".startswith("Py"))  # True
print("a,b,c".split(","))         # ['a', 'b', 'c']

#Important: Strings cannot be changed in place.
word = "Python"
# word[0] = "J"  # TypeError
word = "J" + word[1:]
print(word)      # Jython

'''
B. List (list)
A list is an ordered, mutable collection. It allows duplicate values and can contain different data types.

Common list methods:
Method	            Purpose
append(x)	        Add one item at the end
extend(iterable)	Add multiple items
insert(i, x)	    Insert at an index
remove(x)	        Remove first matching value
pop()	            Remove and return an item
sort()	            Sort the list in place
reverse()	        Reverse the list in place
clear()	            Remove all items
'''
items = [10, 20, 30, 20, "Python"]

print(items[0])     # 10
print(items[1:3])   # [20, 30]

items[0] = 100
items.append(40)
items.remove(20)

print(items)

numbers = [4, 2, 8]

numbers.append(5)
numbers.sort()

print(numbers)  # [2, 4, 5, 8]

'''
C. Tuple (tuple)
A tuple is an ordered, immutable sequence. It allows duplicate values.
'''
student = ("Akash", 20, "CSE")

print(student[0])  # Akash
print(student[1])  # 20
#You cannot reassign a tuple's element:
# student[0] = "Alok"  # TypeError

#A tuple with one element requires a comma:
a = (10,)
b = (10)

print(type(a))  # <class 'tuple'>
print(type(b))  # <class 'int'>

#When to use it: Store fixed records, such as a coordinate (x, y) or a student's fixed set of attributes.

'''
D. Range (range)
range represents an arithmetic progression of integers. It is commonly used in loops and does not store a list of all the generated numbers.
'''
numbers = range(1, 6)
print(list(numbers))  # [1, 2, 3, 4, 5]

'''
Syntax:
range(start, stop, step)
start: starting value, inclusive; defaults to 0.
stop: ending boundary, exclusive.
step: increment or decrement; defaults to 1
'''
print(list(range(2, 11, 2)))
# [2, 4, 6, 8, 10]

print(list(range(5, 0, -1)))
# [5, 4, 3, 2, 1]
