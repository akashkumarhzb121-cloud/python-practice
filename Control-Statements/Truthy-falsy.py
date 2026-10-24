#8. Truthy and falsy values
'''
Python conditions don't have to contain only True or False. Python also evaluates other values according to their truth value.

Common falsy values include:
- False
- None
- 0 and 0.0
- "" (empty string)
- [ ] (empty list)
- {} (empty dictionary)
- set() (empty set)
Most other values are truthy.
'''
name = ""

if name:
    print("Name entered")
else:
    print("Name is empty")


numbers = [10, 20, 30]
if numbers:
    print("List has data")