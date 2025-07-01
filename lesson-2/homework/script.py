#1. Age Calculator
# name = input('What id your name? ')
# year = int(input('What is your year of birth? '))

# age = 2025 - year

# print(f'Name: {name}, age: {age}')

#2. Extract Car Names

# txt = 'LMaasleitbtui'
# print(txt[0::2])

# 3. Extract Car Names

# txt = 'MsaatmiazD'
# print(txt[0::2])

# 4. Extract Residence Area

# txt = "I'am John. I am from London"
# print(txt[20:])

# 5. Reverse String

# n = input('Give string: ')
# print(n[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

# n = input('Give string: ')

# a = n.lower().count('a')
# e = n.lower().count('e')
# i = n.lower().count('i')
# o = n.lower().count('o')
# u = n.lower().count('u')

# sum = a + e + i + o + u

# print(f'The number of vowels: {sum}')

# 7. Find Maximum Value

# nums = []
# n = int(input('How many numbers do you want to add?' ))

# k = 0
# while k != n:
#     num = int(input(f'Give number {k+1}: '))
#     nums.append(num)
#     k += 1;

# print(max(nums))

# 8. Check Palindrome

# n = input('Give string: ')
# k = n[::-1]
# if k == n:
#     print('It is polindrome')
# else:
#     print('It is not polindrome')

# 9. Extract Email Domain

# mail = input('Enter email: ')
# n = mail.index('@')

# domain = mail[n+1:]

# print(f'Your domain is {domain}')

# 10. Generate Random Password
# import random
# import string

# all_char = string.ascii_letters + string.digits + string.punctuation
# len = int(input('Length of your password: '))
# pd = ''.join(random.choices(all_char, k=len))
# print(f'This is your password: {pd}')



