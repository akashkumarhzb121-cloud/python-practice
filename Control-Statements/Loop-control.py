#12. Loop-control statements
#These statements change the normal execution of a loop.

#break — stop the loop and exit it
for i in range(1, 6):
    if i == 4:
        break
    print(i)

#continue — skip the current iteration and continue with the next one
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#pass — do nothing, pass is a placeholder statement. It does not stop a loop or skip an iteration.
for i in range(3):
    pass

print("Finished")

#return — exit a function, return exits the current function and optionally sends a value back to the caller.
def check_number(n):
    if n < 0:
        return "Negative"
    return "Zero or positive"

print(check_number(-5))