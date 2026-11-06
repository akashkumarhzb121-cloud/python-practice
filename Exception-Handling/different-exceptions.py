#4. Handling different exceptions
#You can use multiple except blocks to handle different errors separately
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")
'''
If the user enters abc, Python handles ValueError.
If the user enters 0, Python handles ZeroDivisionError.
If the user enters 5, the output is:
20.0
Best practice: Catch specific exceptions rather than using a broad except for everything. This makes bugs easier to find and prevents unrelated failures from being silently hidden.
'''