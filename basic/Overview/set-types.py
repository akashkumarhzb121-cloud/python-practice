#3. Set types
'''
A. Set (set)
A set is a mutable collection of unique elements. It does not support indexing or slicing.
Duplicates are automatically removed.
'''
numbers = {10, 20, 20, 30, 10}

print(numbers)       # {10, 20, 30} (order may vary)
print(len(numbers))  # 3

#Creating an empty set:
a = set()  # Empty set
b = {}     # Empty dictionary, NOT a set

'''
Common set methods:
Method          	Purpose
add(x)	            Add an element
update(iterable)	Add multiple elements
remove(x)	        Remove an element; raises error if absent
discard(x)      	Remove if present; no error if absent
pop()	            Remove and return an arbitrary element
clear()	            Remove all elements
'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric difference: {1, 2, 5, 6}

'''
B. Frozen set (frozenset)
A frozenset is an immutable set. Once created, you cannot add or remove elements.
'''
A = frozenset([1, 2, 3, 3])

print(A)       # frozenset({1, 2, 3})
print(2 in A)  # True
# A.add(4)  # AttributeError(This fails because frozen sets cannot be modified)

#still perform set operations
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A | B)  # frozenset({1, 2, 3, 4, 5})

'''
Set     vs       frozenset
Feature	:                    set	                frozenset
Mutable	:                   Yes	                No
Duplicates:             	Removed         	Removed
Indexing:	                No	                No
Can be a dictionary key:	No	                Yes, if its elements permit hashing
Add/remove elements: 	    Yes	                No

A frozen set is useful when you need an immutable set, including as a dictionary key or as an element of another set.
'''