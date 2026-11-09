#5. Appending to a file
#Use "a" mode to add content without deleting the existing contents.
with open("notes.txt", "a") as file:
    file.write("Practising every day\n")

'''
If the file previously contained two lines, the new line is added at the end.

This is useful for:
- Application logs.
- Saving new records.
- Adding activity history.
- Recording results from repeated program runs.
Unlike "w", append mode preserves existing content.
'''
