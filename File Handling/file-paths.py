#8. Working with file paths
'''
A relative path such as "students.txt" is resolved relative to the program's current working directory.

You can inspect that directory using os:
'''
import os

print(os.getcwd())

#For cross-platform path construction, pathlib is often more convenient:
from pathlib import Path

file_path = Path("data") / "students.txt"

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
'''
This expects the file to exist at the data/students.txt path relative to the current working directory.

Using encoding="utf-8" is a good practice for text files when you want consistent handling of common international characters.
'''

#9. Useful file methods
'''
Method	            Purpose
read()	            Reads content
readline()	        Reads one line
readlines()	        Reads all lines into a list
write(text)	        Writes a string
writelines(lines)	Writes an iterable of strings
seek(position)	    Moves the file cursor
tell()	            Returns the current cursor position
close()	            Closes the file

Example of tell() and seek():
'''
with open("sample.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    file.seek(0)
    print(file.read(5))
#Assuming the file contains at least five characters, the first and final reads return the same first five characters. The exact cursor positions depend on the file and text encoding.