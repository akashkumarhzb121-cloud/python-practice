#11. Looping statements

# A. for loop
# A for loop iterates over the items in an iterable, such as a list, string, or range.

for i in range(1, 6):
    print(i)
#range(1, 6) produces integers from 1 through 5; the stop value 6 is excluded.

subjects = ["Python", "SQL", "Statistics"]

for subject in subjects:
    print(subject)

#B. while loop
#A while loop repeats as long as its condition is true

i = 1

while i <= 5:
    print(i)
    i += 1

#C. Using a decision inside a loop
for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")