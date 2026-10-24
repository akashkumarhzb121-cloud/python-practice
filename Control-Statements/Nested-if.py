#6. Nested if statements
'''
A nested if is an if statement inside another if statement. It is useful when a decision depends on an earlier decision.

Example: check eligibility for a course.
'''
age = 20
marks = 80

if age >= 18:
    if marks >= 60:
        print("Eligible for admission")
    else:
        print("Marks are insufficient")
else:
    print("Age requirement not met")