#7. Strings are immutable
'''
This is a very important Python concept.

Immutable means the original string cannot be changed character by character after creation.
'''
text = "Python"

# text[0] = "J"  # TypeError

text = "J" + text[1:]
print(text)  # Jython

#Here, Python creates a new string and reassigns text. It doesn't modify the original string.

#String methods also return new strings instead of changing the original:
name = "akash"

result = name.upper()

print(name)    # akash
print(result)  # AKASH

#8. Length and membership
#len(),Returns the number of characters in a string, including spaces.
text = "Hello Python"

print(len(text))  # 12

#in and not in,Check whether a substring exists.
text = "Python Programming"

print("Python" in text)      # True
print("Java" in text)        # False
print("Java" not in text)    # True

#These checks are case-sensitive:
print("python" in "Python")  # False

#9. Practical program: clean a name
name = input("Enter your full name: ")

name = name.strip()
name = name.title()

print("Your name is:", name)