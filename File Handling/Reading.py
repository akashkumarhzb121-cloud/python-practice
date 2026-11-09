#3. Reading a file
'''
First, suppose students.txt contains:
Akash
Rahul
Priya
'''
#A. Read the entire file with read()
with open("students.txt", "r") as file:
    content = file.read()
    print(content)
#read() returns the file's contents as a string.

#B. Read one line with readline()
with open("students.txt", "r") as file:
    print(file.readline())
    print(file.readline())
#This reads the first two lines. Each returned line normally includes its newline character, if present.

#C. Read all lines with readlines()
with open("students.txt", "r") as file:
    lines = file.readlines()
    print(lines)
#readlines() returns a list of strings. For large files, avoid loading every line into memory if you can process the file one line at a time.

#D. Iterate through a file line by line
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
#strip() removes leading and trailing whitespace, including the newline., This approach is memory-efficient for large text files.
