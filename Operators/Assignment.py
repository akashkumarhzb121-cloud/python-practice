#3. Assignment operators
x = 10
print(x)  # 10

'''
Assignment operators assign a value to a variable or update its current value.
Compound    assignment operators
Operator	Equivalent expression
x += 5	        x = x + 5
x -= 5	        x = x - 5
x *= 5	        x = x * 5
x /= 5      	x = x / 5
x //= 5	        x = x // 5
x %= 5	        x = x % 5
x **= 2     	x = x ** 2
'''
x = 10

x += 5
print(x)  # 15

x *= 2
print(x)  # 30

x -= 10
print(x)  # 20

#How it works: Python calculates the new value and updates the variable. For mutable objects such as lists, an in-place operation can also modify the existing object.

# Multiple assignment
# Python allows assigning values to multiple variables in one statement.
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30
#We can also swap values without a temporary variable:
a = 10
b = 20

a, b = b, a
print(a, b)  # 20 10