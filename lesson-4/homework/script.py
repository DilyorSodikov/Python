# Homeworks:

# # Python Dictionary and Set Exercises

# ## Dictionary Exercises

# ### 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

# my_dict = {
#     'a': 5,
#     'b': 2,
#     'c': 9,
#     'd': 1
# }


# sort_1 = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# sort_2 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
# print(sort_1)
# print(sort_2)
# ### 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

# **Sample Dictionary:**
# ```python
# {0: 10, 1: 20}
# ```
# dict_1 = {
#     '0' : 10,
#     '1' : 20,
# }

# dict_1['2'] = 30

# print(dict_1)

# **Expected Result:**
# ```python
# {0: 10, 1: 20, 2: 30}
# ```

# ### 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# **Sample Dictionaries:**
# ```python
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# # ```

# dic1.update(dic2)
# dic1.update(dic3)

# print(dic1)

# **Expected Result:**
# ```python
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# ```

# ### 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.

# **Sample Dictionary (n = 5):**
# ```python
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```

# dict = {}
# n = 5
# k = 1

# while k != n:
#     dict[k] = k*k
#     k += 1

# print(dict)

# ### 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

dict = {}
n = 16
k = 1

while k != n:
    dict[k] = k*k
    k += 1

print(dict)

# **Expected Output:**
# ```python
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# ```

# ## Set Exercises

# ### 1. Create a Set
# Write a Python program to create a set.

# set_1 = {'1','2','3','4','5'}
# print(set_1)

# ### 2. Iterate Over a Set
# Write a Python program to iterate over sets.

# set_1 = {'1','2','3','4','5'}

# for n in set_1:
#     print(n)

# ### 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

# set_1 = {'1','2','3','4','5'}

# set_1.add('6')
# print(set_1)

# ### 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

# set_1 = {'1','2','3','4','5'}

# set_1.remove('1')
# print(set_1)
# ### 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

# set_1 = {'1','2','3','4','5'}

# set_1.discard('4')
# print(set_1)
