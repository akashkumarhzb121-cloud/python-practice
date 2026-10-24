#10. The match-case statement
'''
Python 3.10 and later support match-case, which can select a branch based on the structure or value of an object.
'''
choice = 2

match choice:
    case 1:
        print("Add")
    case 2:
        print("Update")
    case 3:
        print("Delete")
    case _:
        print("Invalid choice")

'''
The _ case acts as a catch-all pattern when no earlier case matches. Unlike a traditional switch in some languages, Python's match supports structural pattern matching, not just simple value comparisons.

Use if-elif for ranges and general Boolean conditions; use match-case when matching distinct values or patterns makes the code clearer.
'''