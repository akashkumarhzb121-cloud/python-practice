#7. Combining conditions with logical operators

#and — both conditions must be true
age = 21
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

#or — at least one condition must be true
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Holiday")
else:
    print("Working day")

#not — reverses a condition
is_raining = False

if not is_raining:
    print("Go for a walk")