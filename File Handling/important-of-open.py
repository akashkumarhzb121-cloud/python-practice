#6. Why is with open() important?
#You may see this pattern:
file = open("notes.txt", "r")
content = file.read()
file.close()
#The problem is that if an exception occurs before close(), the file might remain open longer than intended.

#A better approach is:
with open("notes.txt", "r") as file:
    content = file.read()
'''
The with statement ensures the file is closed when execution leaves the block, including when an exception occurs.

Industry best practice: Prefer with open(...) for ordinary file operations.
'''