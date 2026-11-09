#10. Binary file handling
'''
Text files store readable text. Binary files store bytes and are commonly used for images, PDFs, audio, and other non-text data.

Example: copying an image file.
'''
with open("photo.jpg", "rb") as source:
    data = source.read()

with open("photo_copy.jpg", "wb") as destination:
    destination.write(data)

'''
- "rb" reads bytes.
- "wb" writes bytes.
- data is a bytes object.
For very large files, copying in chunks is better than reading the entire file into memory.
'''
#11. Practical example: Student marks record
# Save the first student record
with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Akash,85\n")

# Add another student record
with open("students.txt", "a", encoding="utf-8") as file:
    file.write("Rahul,92\n")

# Read all records
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, marks = line.strip().split(",")
        print(f"{name} scored {marks} marks")
'''
Let's combine writing, reading, and appending.
This demonstrates a simple way to store records in a text file. In a larger application, CSV, JSON, or a database may be a better choice depending on the data structure and requirements.
'''
#12. File handling for Data Science
'''
File handling is one of the first steps in many data workflows.
Read data
Load a CSV or text file from disk.

Process data
Clean values, calculate statistics, and analyse patterns.

Save results
Write summaries, logs, or output files.
For example, reading CSV data manually:
'''
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["marks"])
#This expects a CSV with headers named name and marks. For larger analytical tasks, you'll likely use the Pandas library:
import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())
#Pandas makes it much easier to filter, clean, transform, and analyse tabular data.