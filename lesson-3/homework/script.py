# # Homework: List and Tuple Exercises

# ## 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

# list_1 = ['Banana', 'Apple', 'Orange', 'Cherry', 'Pineapple']
# print(list_1[2])

# ## 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

# list_1 = ['Banana', 'Apple', 'Orange', 'Cherry', 'Pineapple']
# list_2 = ['Banan', 'Olma', 'Apelsin', ' Uzum', 'Ananas']
# list_3 = list_1 + list_2
# print(list_3)

# ## 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

# list_1 = ['Banana', 'Apple', 'Orange', 'Cherry', 'Pineapple']
# print(list_1[0])
# print(list_1[-1])
# print(list_1[int(len(list_1)/2)])

# ## 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

# list_1 = ['Movie_1', 'Movie_2', 'Movie_3', 'Movie_4', 'Movie_5']
# tuple_1 = tuple(list_1)
# print(tuple_1)

# ## 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

# cities = [
#     "Tashkent",
#     "Samarkand",
#     "Bukhara",
#     "Khiva",
#     "Andijan",
#     "Namangan",
#     "Fergana",
#     "Nukus",
#     "Termez",
#     "Jizzakh"
# ]

# if 'Paris' in cities:
#     print('Paris')
# else:
#     print('There is no such city')

# ## 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

# cities = [
#     "Tashkent",
#     "Samarkand",
#     "Bukhara",
#     "Khiva",
#     "Andijan",
#     "Namangan",
#     "Fergana",
#     "Nukus",
#     "Termez",
#     "Jizzakh"
# ]

# cities_2 = cities[:]
# print(cities_2)

# ## 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

# cities = [
#     "Tashkent",
#     "Samarkand",
#     "Bukhara",
#     "Khiva",
#     "Andijan",
#     "Namangan",
#     "Fergana",
#     "Nukus",
#     "Termez",
#     "Jizzakh"
# ]

# first = cities.pop(0)
# last = cities.pop()
# cities.insert(0, last)
# cities.append(first)
# print(cities)

# ## 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

# tuple_1 = (range(1,11))
# print(tuple_1[3:7])

# ## 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

# colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Yellow",
#     "Orange",
#     "Purple",
#     "Pink",
#     "Brown",
#     "Black",
#     "White"
# ]

# print(colors.count('Blue'))

# ## 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

# animals = [
#     "Lion",
#     "Tiger",
#     "Elephant",
#     "Zebra",
#     "Giraffe",
#     "Kangaroo",
#     "Panda",
#     "Wolf",
#     "Bear",
#     "Fox"
# ]

# print(animals.index('Lion'))

# ## 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

# animals = (
#     "Lion",
#     "Tiger",
#     "Elephant",
#     "Zebra",
#     "Giraffe",
#     "Kangaroo",
#     "Panda",
#     "Wolf",
#     "Bear",
#     "Fox"
# )

# colors = (
#     "Red",
#     "Blue",
#     "Green",
#     "Yellow",
#     "Orange",
#     "Purple",
#     "Pink",
#     "Brown",
#     "Black",
#     "White"
# )

# comb = animals + colors
# print(comb)


# ## 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

# animals = (
#     "Lion",
#     "Tiger",
#     "Elephant",
#     "Zebra",
#     "Giraffe",
#     "Kangaroo",
#     "Panda",
#     "Wolf",
#     "Bear",
#     "Fox"
# )

# colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Yellow",
#     "Orange",
#     "Purple",
#     "Pink",
#     "Brown",
#     "Black",
#     "White"
# ]

# print(len(colors))
# print(len(animals))

# ## 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
# animals = (
#     "Lion",
#     "Tiger",
#     "Elephant",
#     "Zebra",
#     "Giraffe",
#     "Kangaroo",
#     "Panda",
#     "Wolf",
#     "Bear",
#     "Fox"
# )

# animals = list(animals)
# print(animals)

# ## 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

# numbers = (5, 12, 8, 3, 21, 7, 14, 9, 0, 18)

# print(max(numbers))
# print(min(numbers))

# ## 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

# numbers = (5, 12, 8, 3, 21, 7, 14, 9, 0, 18)

# reversed_numbers = tuple(reversed(numbers))
# print(reversed_numbers)



