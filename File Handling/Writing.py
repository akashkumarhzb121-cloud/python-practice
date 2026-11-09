#4. Writing to a file
#Use "w" mode to write new content.
with open("notes.txt", "w") as file:
    file.write("Learning Python\n")
    file.write("Learning file handling\n")

'''
The file now contains:
Learning Python
Learning file handling

The \n character creates a new line.
Remember: Opening an existing file in "w" mode truncates it before writing.
'''