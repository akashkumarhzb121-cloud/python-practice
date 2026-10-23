#5. Logical operators
'''
Logical operators combine or reverse conditions.
Operator	 Meaning	                                    Example
and	        True when both conditions are true	        True and False → False
or	        True when at least one condition is true	True or False → True
not	        Reverses a truth value	                    not True → False
'''

#Example: checking eligibility
# Suppose a student must be at least 18 years old and have at least 60 marks.
age = 20
marks = 75

print(age >= 18 and marks >= 60) #both condition needs to be true
# True

#use of or:
print(age >= 18 or marks >= 90) #at least one condition needs to be true
# True

#use of not:
is_absent = False
print(not is_absent)  # True

#Python may skip evaluating the second operand when the first one determines the result.
x = 0

print(x != 0 and 10 / x > 2)
# False, Python stops after x != 0 evaluates to False. It does not evaluate 10 / x, so no division-by-zero error occurs