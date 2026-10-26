#3. String indexing
#Each character has an index, starting at 0.
text = "PYTHON"

print(text[0])  # P
print(text[1])  # Y
print(text[5])  # N

#Negative indexing starts from the end:
text = "PYTHON"

print(text[-1])  # N
print(text[-2])  # O
print(text[-6])  # P

#If you access an index outside the string's range, Python raises an IndexError.
text = "Python"
# print(text[10])  # IndexError