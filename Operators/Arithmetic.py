#2. Arithmetic operators
'''
Arithmetic operators perform mathematical calculations.
Operator	Name	                Example	Result
+	        Addition	            10 + 3	13
-       	Subtraction	            10 - 3	7
*       	Multiplication	        10 * 3	30
/       	Division	            10 / 3	3.333…
//	        Floor division	        10 // 3	3
%	        Modulus (remainder)	    10 % 3	1
**	        Exponentiation	        2 ** 3	8
'''
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

#Understand /, //, and %
'''
Division /
Gives the ordinary division result.
10 / 3 = 3.333333...


Floor division //
Rounds the quotient down toward negative infinity.
10 // 3 = 3
-10 // 3 = -4


Modulus %
Gives the remainder consistent with floor division.
10 % 3 = 1
-10 % 3 = 2
'''

#example: even or odd
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#example: exponentiation
print(2 ** 4)  # 16
print(5 ** 2)  # 25
#** means “raise to the power of.” Therefore, 2 ** 4 means \(2^4\), or \(2 \times 2 \times 2 \times 2\).