'''

Feature	            Lists (list)	                                Tuples (tuple)
Syntax	            Square brackets: ['apple', 'banana']	            Parentheses: ('apple', 'banana')
Mutability	        Mutable (can add, remove, or edit items)	        Immutable (fixed data structure)
Memory Allocation	Higher overhead (allocates extra space for growth)	Lighter footprint (allocates the exact space needed)
Performance	        Slower  instantiation and iteration	                Faster instantiation and iteration
Built-in Methods	Many (.append(), .extend(), .pop(), .sort())	    Few (only .count() and .index())
Dictionary Keys	    No  (unhashable type)	                            Yes (if the tuple's elements are also immutable)


- List: ordered, mutable, written with [].
- Tuple: ordered, immutable, commonly written with ().
- Both allow duplicates, mixed data types, indexing, and slicing.
- List methods include append(), insert(), remove(), pop(), and sort().
- Tuple methods include count() and index().
- list() converts an iterable into a list; tuple() converts an iterable into a tuple.
- Tuple unpacking assigns its elements to individual variables.
- A tuple can contain mutable objects, such as lists.
- Choose a list for changeable collections and a tuple for fixed collections.
'''
#1. Mutability (Changing Elements), You can freely modify a list, but attempting to modify a tuple will result in a TypeError.
#LISTS 
fruits_list = ["apple", "banana", "cherry"]
fruits_list[1] = "blueberry"  # Allowed!
print(fruits_list)  # Output: ['apple', 'blueberry', 'cherry']

#TUPLES
fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple[1] = "blueberry"  # ❌ Throws TypeError: 'tuple' object does not support item assignment

#2. Adding and Removing Elements, Lists have built-in methods to grow or shrink in size. Tuples are completely fixed.
#LISTS
numbers = [1, 2, 3]
numbers.append(4)  # Add an item
numbers.remove(2)  # Remove an item
print(numbers)  # Output: [1, 3, 4]

#TUPLES
coordinates = (10, 20)
# coordinates.append(30)  # ❌ AttributeError: 'tuple' object has no attribute 'append'

#3. Using as Dictionary Keys, Because tuples cannot change, they are "hashable" and can be used as keys in a Python dictionary. Lists cannot.
#TUPLES AS KEYS
# Valid: Using an (x, y) coordinate tuple as a key
locations = {(40.7128, -74.0060): "New York"}
print(locations[(40.7128, -74.0060)])  # Output: New York

#LISTS AS KEYS
# invalid_dict = {[1, 2]: "Data"}  # ❌ Throws TypeError: unhashable type: 'list'

#4. The Single-Element Trap, When creating a tuple with only one item, you must include a trailing comma, otherwise Python treats it as a regular string or number wrapped in parentheses.
just_a_string = "apple"  # Type: str
correct_tuple = ("apple",)  # Type: tuple
