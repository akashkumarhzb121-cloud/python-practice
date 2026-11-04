#5. Instance attributes vs class attributes
#These are two different ways to store data.
class Student:
    college = "GIT Jaipur"  # Class attribute

    def __init__(self, name):
        self.name = name    # Instance attribute

s1 = Student("Akash")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)
print(s1.college)
print(s2.college)
'''
Instance attribute	                Class attribute
Belongs to a particular instance	Defined on the class
Commonly stores individual data	    Commonly stores shared data
Example: student name	            Example: college name

Be careful with mutable class attributes such as lists: all instances may share the same list unless you create a separate list for each object.
'''