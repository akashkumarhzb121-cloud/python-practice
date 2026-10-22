#7. Type conversion (type casting)
'''
Sometimes you need to convert one data type into another.
Function	Purpose	            Example
int()	Convert to integer	int("25") → 25
float()	Convert to float	float("2.5") → 2.5
str()	Convert to string	str(100) → "100"
bool()	Convert to Boolean	bool(1) → True
complex()	Create a complex number	complex(2, 3) → (2+3j)
'''
a = "50"
b = int(a)

print(a, type(a))  # 50 <class 'str'>
print(b, type(b))  # 50 <class 'int'>
print(b + 10)      # 60

#Important conversion mistakes
print(int(5.9))    # 5
print(float(5))    # 5.0
print(int("25"))   # 25

# int("hello")     # ValueError

#8. Taking input and understanding its type
'''
The input() function returns a string, even if the user enters digits.
vIf the user enters 20, the type is still str.
'''
age = input("Enter your age: ")

print(age)
print(type(age))

#To use the input as a number:
age2 = int(input("Enter your age: "))
print(age2 + 1)
print(type(age2))

#For decimal values:
marks = float(input("Enter marks: "))
print(marks)