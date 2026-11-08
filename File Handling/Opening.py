#2. Opening a file with open()
'''
Python's built-in open() function opens a file and returns a file object.

Syntax:
file = open("filename.txt", "mode")

The two important arguments are:
- Filename/path: Which file to open.
- Mode: What you want to do with the file.
Common file modes
Mode	Meaning
"r"	Read an existing file
"w"	Write; create or overwrite a file
"a"	Append; add content at the end
"x"	Create a new file; fail if it already exists
"b"	Binary mode, e.g. "rb"
"t"	Text mode; default, e.g. "rt"
"r+"	Read and write without truncating the existing file initially

Important: "w" can erase the previous contents of a file. Use it carefully.
'''
file = open("filename.txt", "mode")