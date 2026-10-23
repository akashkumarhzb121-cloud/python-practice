#3. Creating an array
'''
The syntax is:
import array
arr = array.array(typecode, elements)
'''
import array

numbers = array.array('i', [10, 20, 30, 40])

print(numbers)
print(numbers[0])  # 10
print(numbers[2])  # 30

'''
Here, 'i' specifies a signed integer type.
Common typecodes include 'i' for signed integers, 'f' for single-precision floats, and 'd' for double-precision floats. Exact supported sizes can depend on the platform.
'''
#4. Accessing and modifying elements
import array

arr = array.array('i', [10, 20, 30])
arr[0] = 100

print(arr)      # array('i', [100, 20, 30])
print(arr[-1])  # 30

#5. Important array operations
import array

arr = array.array('i', [10, 20, 30])

arr.append(40)       # Add one element #array('i', [10, 15, 30, 40])
arr.insert(1, 15)    # Insert at index 1
arr.remove(20)       # Remove first matching value
arr.pop()            # Remove last element

print(arr)

#Other useful operations
print(len(arr))       # Number of elements
print(arr.index(15))  # Index of value 15

#6. Traversing an array
import array

arr = array.array('i', [10, 20, 30, 40])

for item in arr:
    print(item)

#7. NumPy arrays — important for Data Science
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr + 5)
print(arr * 2)

'''
NumPy is a popular Python library for numerical computing. Its arrays support efficient element-wise operations and multidimensional data.
Unlike a normal Python list, NumPy performs these operations on every element without requiring an explicit loop.
'''
#Two-dimensional NumPy array
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)  # (2, 3)
print(arr[0, 1])  # 2