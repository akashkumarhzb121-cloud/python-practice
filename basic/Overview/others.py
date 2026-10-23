#6. Other built-in data types , Python also provides types for binary data and the absence of a value.
'''
A. Complex (complex)
Used for numbers with real and imaginary parts.
The imaginary unit is written as j in Python.
'''
z = 2 + 3j

print(z.real)  # 2.0
print(z.imag)  # 3.0
print(z * z)   # (-5+12j)

'''
B. Boolean (bool)
Represents True or False.
'''
age = 20

print(age >= 18)  # True
print(age < 18)   # False

'''
C. None (NoneType)
Represents the absence of a value.
Use is None to test for None, rather than relying on equality with other values.
'''
result = None

print(result)        # None
print(result is None)  # True

'''
D. Bytes (bytes)
An immutable sequence of byte values, each between 0 and 255.
Bytes are useful when working with files, network communication, and binary data.
'''
data = b"Hello"

print(data)       # b'Hello'
print(data[0])    # 72
print(type(data)) # <class 'bytes'>

'''
E. Bytearray (bytearray)
A mutable sequence of bytes.
Unlike bytes, its individual byte values can be modified.
'''
data = bytearray(b"ABC")

data[0] = 88
print(data)  # bytearray(b'XBC')

'''
F. Memoryview (memoryview)
Provides access to the binary data of a compatible object without making a copy of the underlying data for ordinary views
This can be useful when processing large binary data efficiently.
'''
data = bytearray(b"ABC")
view = memoryview(data)

view[0] = 88
print(data)  # bytearray(b'XBC')

numbers = [10, 20, 30]  # Iterable

it = iter(numbers)      # Iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
#A further next(it) raises StopIteration because there are no more values.