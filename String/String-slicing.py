#4. String slicing
'''
Slicing extracts part of a string.

Syntax:
string[start:stop:step]

start: index to begin at, included.
stop: index to stop before, excluded.
step: number of positions to move each time.
'''

text = "Python"

print(text[0:3])   # Pyt
print(text[2:6])   # thon
print(text[:4])    # Pyth
print(text[2:])    # thon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP

#Remember: The stop index is excluded. Slicing is useful for extracting parts of text without changing the original string