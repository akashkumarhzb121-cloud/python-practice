#4. Comparison operators
'''
Comparison operators compare two values and normally return a Boolean result: True or False.
Operator	Meaning	                    Example	Result
==	        Equal to	                5 == 5	True
!=	        Not equal to	            5 != 3	True
>	        Greater than	            5 > 3	True
<	        Less than	                5 < 3	False
>=	        Greater than or equal to	5 >= 5	True
<=	        Less than or equal to	    3 <= 5	True
'''
age = 20

print(age == 20)  # True
print(age != 18)  # True
print(age >= 18)  # True
print(age < 18)   # False

#Difference between = and ==
x = 10      # Assignment
print(x == 10)  # Comparison: True

#Chained comparisons
#Python lets you combine comparisons naturally:
age = 20
print(18 <= age <= 60)  # True