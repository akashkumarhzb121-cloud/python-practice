#5. The if-elif-else statement
'''
What if there are more than two possible outcomes? Use elif, meaning “else if.”

Example: assign a grade based on marks.
'''
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")