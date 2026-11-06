#6. The finally block
#The finally block runs whether or not an exception occurred. It is commonly used for cleanup tasks.
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")
'''
Even if the file is missing, the finally block executes.

One detail: in this example, if the file opens successfully, it should also be closed. For normal file handling, Python's with statement is usually better because it closes the file automatically.
'''
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")
'''
The file is closed automatically when execution leaves the with block.
Quick comparison
Block	When it runs
try	Runs code that might raise an exception
except	Handles a matching exception
else	Runs if try succeeds without an exception
finally	Runs during normal cleanup, whether an exception occurred or not
'''