#5. The map() function
'''
This is slightly different from the collection types above. map() is a built-in function that applies another function to every item in an iterable. It returns a map iterator.
Example: Convert strings into integers.
'''
numbers = ["10", "20", "30"]

result = map(int, numbers)

print(list(result))
# [10, 20, 30]

'''
How it works:
1. numbers contains three strings.
2. int is the function passed to map().
3. map() applies int() to each string.
4. list() consumes the iterator and displays the converted values.
'''

numbers = [1, 2, 3, 4]

squares = map(lambda x: x ** 2, numbers)
#We can often use a list comprehension instead:
# squares = [x ** 2 for x in numbers]
print(list(squares))
# [1, 4, 9, 16]
#Here, lambda x: x ** 2 is a small anonymous function that squares its input.

#Remember: A map object is an iterator, not a list. It is usually consumed as you iterate over it, so converting it to a list again after full consumption typically produces an empty list.

