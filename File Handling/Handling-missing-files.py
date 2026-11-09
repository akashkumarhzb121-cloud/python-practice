#7. Handling missing files
#If you try to read a file that doesn't exist, Python raises FileNotFoundError.
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The requested file was not found.")

'''
You can combine file handling with the exception-handling concepts from the previous lesson.

For writing files, also remember that permission errors or an unavailable storage device can cause other exceptions.
'''