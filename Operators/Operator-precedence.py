#9. Operator precedence
'''
When an expression contains multiple operators, Python follows precedence rules to determine which operation happens first. Parentheses can make the intended order explicit
'''
result = 2 + 3 * 4
print(result)  # 14

#Multiplication occurs before addition.
result = (2 + 3) * 4
print(result)  # 20

'''
A simplified order to remember, from higher to lower precedence:

| Order | Operators |

| 1     | Parentheses () |
| 2     | Exponentiation ** |
| 3     | Unary +, -, ~ |
| 4     | *, /, //, % |
| 5     | +, - |
| 6     | Bitwise shifts <<, >> |
| 7     | Bitwise &, ^, | |
| 8     | Comparisons, in, is |
| 9     | not |
| 10    | and |
| 11    | or |
'''
print(10 + 2 * 3)          # 16
print((10 + 2) * 3)        # 36
print(5 > 2 and 8 > 4)     # True