# # Homeworks

# ## 1. Modify String with Underscores
# Given a string `txt`, insert an underscore (`_`) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

# ### Examples
# **Input:** `hello`
# **Output:** `hel_lo`

# **Input:** `assalom`
# **Output:** `ass_alom`

# **Input:** `abcabcabcdeabcdefabcdefg`
# **Output:** `abc_abc_abcd_abcd_abcdef`

# ---

# word = input('Enter string: ')
# list_1 = []
# vowels = "aeiouAEIOU"
# n = 0
# count = 0

# while n < len(word):
#     list_1.append(word[n])
#     count += 1

#     if count == 3:
#         if n + 1 >= len(word):
#             break
#         if word[n + 1] in vowels or word[n + 1] == '_':
#             list_1.append(word[n+1])
#             n += 1
#         list_1.append('_')
#         count = 0
#     n += 1
    
# print(''.join(list_1))


# ## 2. Integer Squares Exercise

# ### Task
# The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers `i` where `0 <= i < n`, print `i^2`.

# ### Example Input
# ```
# 5
# ```

# ### Example Output
# ```
# 0
# 1
# 4
# 9
# 16
# ```

# ### Input Format
# The first and only line contains the integer, `n`.

# ### Constraints
# - `1 <= n <= 20`

# ### Output Format
# Print `n` lines, one corresponding to each `i^2` where `0 <= i < n`.

# ---
# numb = int(input('Give a number: '))
# n = 0

# while n < numb:
#     gd = n ** 2
#     print(gd)
#     n += 1



# ## 3. Loop-Based Exercises

# ### Exercise 1: Print first 10 natural numbers using a while loop

# n = 1
# while n <= 10:
#     print(n)
#     n += 1

# ### Exercise 2: Print the following pattern
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```

# list_1 = [1,2,3,4,5]
# k = 0
# for n in list_1:
#     print(' '.join(str(x) for x in list_1[0:k+1]))
#     k += 1

# ### Exercise 3: Calculate sum of all numbers from 1 to a given number
# **Example:**
# ```
# Enter number 10
# Sum is: 55
# ```

# numb = int(input('Give a number: '))
# n = 1
# k = 0 
# while n <= numb:
#     k += n
#     n += 1
# print(k)


# ### Exercise 4: Print multiplication table of a given number
# **Example:**
# ```
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# ```

# numb = int(input('Give a number: '))
# n = 1

# while n <= numb:
#     print(n*2)
#     n += 1


# ### Exercise 5: Display numbers from a list using a loop
# **Given:**
# ```python
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# **Expected Output:**
# ```
# 75
# 150
# 145
# ```

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for n in numbers:
#     if n > 50 and n < 160:
#         print(n)


# ### Exercise 6: Count the total number of digits in a number
# **Example:**
# ```
# 75869
# Output: 5
# ```

# numb = str(input('Give a number: '))
# n = 0

# for k in numb:
#     n += 1

# print(n)


# ### Exercise 7: Print reverse number pattern
# ```
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# ```

# list_1 = [1,2,3,4,5]

# list_2 = list(reversed(list_1))
# i = 0
# for n in list_2:
#     print(' '.join(str(x) for x in list_2[i:len(list_2)]))
#     i += 1

# ### Exercise 8: Print list in reverse order using a loop
# **Given:**
# ```python
# list1 = [10, 20, 30, 40, 50]
# ```
# **Expected Output:**
# ```
# 50
# 40
# 30
# 20
# 10
# ```

# list1 = [10, 20, 30, 40, 50]
# list2 = list(reversed(list1))

# for n in list2:
#     print(n)


# ### Exercise 9: Display numbers from -10 to -1 using a for loop
# ```
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# ```

# lisr_1 = list(range(-10, 0))

# for n in lisr_1:
#     print(n)


# ### Exercise 10: Display message “Done” after successful loop execution
# **Example:**
# ```python
# 0
# 1
# 2
# 3
# 4
# Done!
# ```

# list_1 = list(range(0,5))

# for n in list_1:
#     print(n)

# print('Done!')


# ### Exercise 11: Print all prime numbers within a range
# **Example:**
# ```
# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47
# ```
# from sympy import isprime
# first = int(input('From: '))
# second = int(input('To: '))

# print('Prime numbers are: ')

# list_1 = list(range(first, second + 1))

# for n in list_1:
#     if isprime(n) == True:
#         print(n)

# ### Exercise 12: Display Fibonacci series up to 10 terms
# **Example:**
# ```
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
# ```

# a,b = 0, 1
# for n in range(10):
#     print(a, end = ' ')
#     a,b = b, a + b


# ### Exercise 13: Find the factorial of a given number
# **Example:**
# ```
# 5! = 120
# ```

# ---
# numb = int(input('Give number: '))
# n = 1

# for k in range(1,numb + 1):
#     n *= k
# print(n)

# ## 4. Return Uncommon Elements of Lists
# ### Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# ### Examples
# - **Input:** `list1 = [1, 1, 2], list2 = [2, 3, 4]`  
#   **Output:** `[1, 1, 3, 4]`

# - **Input:** `list1 = [1, 2, 3], list2 = [4, 5, 6]`  
#   **Output:** `[1, 2, 3, 4, 5, 6]`

# - **Input:** `list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]`  
#   **Output:** `[2, 2, 5]`

# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]

# list_3 = []

# for n in list1:
#     if n not in list2:
#         list_3.append(n)

# for n in list2:
#     if n not in list1:
#         list_3.append(n)

# print(list_3)
