#8. Bitwise operators
'''
Bitwise operators work on the binary representation of integers.
Computers represent integers using bits (0 and 1). Bitwise operators perform operations on these bits.

| Operator      | Name          | Meaning 

| &             | AND           | Bit is 1 if both bits are 1 |
| |             | OR            | Bit is 1 if either bit is 1 |
| ^             | XOR           | Bit is 1 if the bits differ |
| ~             | NOT           | Inverts the integer's bits |
| <<            | Left shift    | Shifts bits left |
| >>            | Right shift   | Shifts bits right |
Example: AND, OR, and XOR
Take 5 and 3.

Their binary representations are:
5 = 101
3 = 011
'''
a = 5
b = 3

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6

'''
why?
AND: 101 & 011 = 001  -> 1
OR:  101 | 011 = 111  -> 7
XOR: 101 ^ 011 = 110  -> 6
'''

#Left and right shifts
print(5 << 1)  # 10
print(5 >> 1)  # 2
#For non-negative integers, shifting left by one position is equivalent to multiplying by two; shifting right by one position is equivalent to floor-dividing by two.
#Bitwise NOT
print(~5)  # -6
#For Python integers, ~x equals -x - 1. Therefore, ~5 is -6.

#Bitwise operators are useful in low-level programming, binary data processing, and certain algorithms