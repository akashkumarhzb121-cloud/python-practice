#1. What is file handling?
#Imagine you calculate a student's marks using Python.
marks = 85
print(marks)
'''
The value exists while your program runs, but it isn't automatically saved to a file.

With file handling, you can save it:
'''
with open("marks.txt", "w") as file:
    file.write("Student marks: 85")

'''
This creates marks.txt if it doesn't exist, or overwrites it if it already exists.

The file is stored relative to the current working directory unless you provide a path.
'''