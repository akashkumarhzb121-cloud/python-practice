#10. When should you use dictionaries?
#Use a dictionary when you need to associate values with meaningful keys rather than access items only by position.

#Student records
student = {"name": "Akash", "marks": 85}
#Access student details by their field names.


#Counting items
counts = {"apple": 3, "mango": 2}
#Store how many times each item occurs.


#API and JSON data
user = {"id": 101, "active": True}
#Represent structured information exchanged between applications.


#Fast lookups
prices = {"pen": 10, "book": 50}
print(prices["book"])  # 50
#Retrieve a value using its key, typically in average constant time for dictionary lookups.