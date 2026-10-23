#1. What is an array?
'''
An array is a data structure used to store multiple elements under one variable name. In Python, the term “array” can refer to different things:
- List: Python's general-purpose collection, which can store different data types.
- array module: Stores elements of a specified numeric type.
- NumPy array (ndarray): Used for fast numerical calculations and Data Science.
'''
#2. Python list vs array
# List: different data types allowed
my_list = [10, 20, "Akash", 30.5]
print(my_list)

# Array: elements use a specified type
import array

my_array = array.array('i', [10, 20, 30, 40])
print(my_array)

'''
Feature	            List	                             array.array
Data types	        Can be mixed	                     One specified type
Numeric operations	Usually use loops or functions	     Usually use loops or functions
Memory	            Generally more overhead         	 More compact for supported numeric types
Module required	    No	                                 Yes, import array
'''