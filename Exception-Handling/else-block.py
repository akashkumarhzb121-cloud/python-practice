#5. The else block
#The else block runs only if the try block finishes without raising an exception.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)
'''
If the user enters 25, the output is:
You entered: 25

If the user enters hello, the except block runs instead, and the else block is skipped.
Use else for operations that should happen only when the risky operation succeeds.
'''