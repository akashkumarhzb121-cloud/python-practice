#9. Creating a custom exception
#In larger applications, you can define exceptions that describe your own domain-specific errors
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    return balance - amount

try:
    print(withdraw(1000, 1500))
except InsufficientBalanceError as e:
    print(e)

#10. Practical example: Safe calculator
#Let's combine the concepts in a small calculator.
def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a / b

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError:
        print("The second number cannot be zero.")

    else:
        print("Result:", result)

    finally:
        print("Calculator operation finished.")

divide_numbers()

'''
This handles invalid numeric input, division by zero, successful calculations, and a final status message.

In a real application, finally is especially valuable for releasing resources. Here, it simply demonstrates that the cleanup/status block runs regardless of the outcome.

11. Common mistakes to avoid
- Using bare except: everywhere: It can catch unexpected errors, including exceptions you didn't intend to handle. Catch specific exception types when possible.
- Putting everything in try: Keep the try block focused on the operation that might fail.
- Ignoring errors silently: Empty exception handlers make debugging difficult.
- Confusing syntax errors with runtime exceptions: A syntax error generally prevents the code from being parsed; try/except is not a general way to catch malformed Python syntax in the same code block.
- Assuming finally always means success: It executes for cleanup, even when an exception occurred; the exception may still propagate afterward.
'''