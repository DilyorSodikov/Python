# macOS example path - adjust to your actual path
# file_path = '/Users/dilyor/Desktop/Try.txt'

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print("File content:\n", content)
# except FileNotFoundError:
#     print("The file was not found.")
# except PermissionError:
#     print("You don't have permission to access the file.")



# Homework:

# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises

# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# try:
#     a = 10
#     b = 0
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print('ZeroDivisionError')

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     num = int(input("Enter an integer: "))
#     print("You entered:", num)

# except ValueError:
#     print("ValueError: That was not a valid integer.")


# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# try:
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('File not found')

# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# try:
#     x = 5
#     y = "hello"
#     result = x + y  # This will raise: TypeError: unsupported operand type(s) for +: 'int' and 'str'
#     print("Result:", result)
# except TypeError:
#     print("TypeError: Cannot add int and string.")


# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

# try:
#     with open("protected.txt", "w") as file:
#         file.write("Test")
# except PermissionError:
#     print("PermissionError triggered.")


# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

# try:
#     lst = [1, 2, 3]
#     print(lst[5])
# except IndexError:
#     print('IndexError')


# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

# try:
#     num = input("Enter a number (press Ctrl+C to cancel): ")
#     print("You entered:", num)
# except KeyboardInterrupt:
#     print('KeyboardInterrupt')

# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

# try:
#     a = 5
#     b = 0
#     result = a // b
#     print("Result:", result)
# except ArithmeticError:
#     print('ArithmeticError')


# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

# try:
#     with open("/Users/dilyor/Desktop/Try.txt", encoding="ascii") as file:
#         content = file.read()
#         print(content)
# except UnicodeError:
#     print('Error with encoding')


# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

# try:
#     lst = [1, 2, 3]
#     lst.upper() 
# except AttributeError:
#     print('AttributeError')


# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises

# Write a Python program to read an entire text file.

# with open("/Users/dilyor/Desktop/Try.txt") as file:
#     content = file.read()
#     print(content)

# Write a Python program to read first n lines of a file.

# def firts_n(file_name, n):
#     with open(file_name, 'r') as file:
#         for i in range(n):
#             lines = file.readline() 
#             if not lines:
#                 break
#             print(lines.strip())


# firts_n("/Users/dilyor/Desktop/Try.txt", 20)

# Write a Python program to append text to a file and display the text.

# def add_text(file_name, text):
#     with open(file_name, 'a') as file:
#         file.write(text + '\n')
#     with open(file_name, 'r') as file:
#         lines = file.read()
#         print(lines)


# add_text("/Users/dilyor/Desktop/Try.txt", 'Hello World')

# Write a Python program to read last n lines of a file.

# def last_n(file_name, n):
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#         for line in lines[-n:]:
#             print(line)

# last_n("/Users/dilyor/Desktop/Try.txt", 10)

# Write a Python program to read a file line by line and store it into a list.

# def wr_list(file_name):
#     with open(file_name, 'r') as file:
#         lines_list = [line.strip() for line in file]
#     return lines_list

# print(wr_list("/Users/dilyor/Desktop/Try.txt"))
# Write a Python program to read a file line by line and store it into a variable.

# def read_lines_to_variable(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = ""
#             for line in f:
#                 content += line
#         return content
#     except Exception as e:
#         print("An error occurred:", e)

# # Example usage:
# data = read_lines_to_variable('Try.txt')
# print(data)


# Write a Python program to read a file line by line and store it into an array.

# def read_to_array(filename):
#     try:
#         with open(filename, 'r') as f:
#             array = [line.strip() for line in f]
#         return array
#     except Exception as e:
#         print("An error occurred:", e)
#         return []

# # Example usage:
# arr = read_to_array("/Users/dilyor/Desktop/Try.txt")
# print(arr)

# Write a Python program to find the longest words.

# def find_longest_words(filename):
#     try:
#         with open(filename, 'r') as f:
#             words = f.read().split()
#             max_len = max(len(word) for word in words)
#             longest = [word for word in words if len(word) == max_len]
#         return longest
#     except Exception as e:
#         print("An error occurred:", e)
#         return []

# # Example usage:
# print(find_longest_words('/Users/dilyor/Desktop/Try.txt'))


# Write a Python program to count the number of lines in a text file.

# def count_lines(filename):
#     try:
#         with open(filename, 'r') as f:
#             lines = f.readlines()
#         return len(lines)
#     except Exception as e:
#         print("An error occurred:", e)
#         return 0

# # Example usage:
# print(count_lines('/Users/dilyor/Desktop/Try.txt'))


# Write a Python program to count the frequency of words in a file.

# def word_frequency_manual(filename):
#     try:
#         with open(filename, 'r') as f:
#             words = f.read().split()
#             frequency = {}
#             for word in words:
#                 if word in frequency:
#                     frequency[word] += 1
#                 else:
#                     frequency[word] = 1
#             return frequency
#     except Exception as e:
#         print("An error occurred:", e)
#         return {}

# # Example usage
# print(word_frequency_manual('/Users/dilyor/Desktop/Try.txt'))


# Write a Python program to get the file size of a plain file.

# import os

# def get_file_size(filename):
#     try:
#         size = os.path.getsize(filename)
#         return size  # size in bytes
#     except Exception as e:
#         print("An error occurred:", e)
#         return None

# # Example usage:
# print(get_file_size('/Users/dilyor/Desktop/Try.txt'), "bytes")


# Write a Python program to write a list to a file.

# data = ['apple', 'banana', 'cherry']

# with open('/Users/dilyor/Desktop/Try.txt', 'w') as f:
#     for item in data:
#         f.write(item + '\n')


# Write a Python program to copy the contents of a file to another file.

# with open('/Users/dilyor/Desktop/Try.txt', 'r') as source, open('copy_try.txt', 'a') as dest:
#     dest.write(source.read())

# import os
# abs_path = os.path.abspath('copy_try.txt')
# print("Full path:", abs_path)

# Write a Python program to combine each line from the first file with the corresponding line in the second file.

# with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('combined.txt', 'w') as out:
#     for line1, line2 in zip(f1, f2):
#         out.write(line1.strip() + ' ' + line2)


# Write a Python program to read a random line from a file.

# import random

# with open('Try.txt', 'r') as f:
#     lines = f.readlines()
#     print(random.choice(lines).strip())


# Write a Python program to assess if a file is closed or not.

# f = open('Try.txt', 'r')
# print("Closed?", f.closed)  # Should be False
# f.close()
# print("Closed?", f.closed)  # Should be True


# Write a Python program to remove newline characters from a file.

# with open('Try.txt', 'r') as f:
#     lines = f.readlines()

# with open('no_newlines.txt', 'w') as f:
#     for line in lines:
#         f.write(line.strip())


# Write a Python program that takes a text file as input and returns the number of words in a given text file.

# Note: Some words can be separated by a comma with no space.

# with open('Try.txt', 'r') as f:
#     content = f.read()
#     words = content.replace(',', ' ').split()
#     print("Word count:", len(words))


# Write a Python program to extract characters from various text files and put them into a list.

# char_list = []

# for filename in ['Try.txt', 'copy_try.txt']:
#     with open(filename, 'r') as f:
#         char_list.extend(list(f.read()))

# print(char_list)


# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

# import string

# for letter in string.ascii_uppercase:
#     with open(f'{letter}.txt', 'w') as f:
#         f.write(f"This is file {letter}.txt")


# Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

# import string

# letters_per_line = 5

# with open('alphabet.txt', 'w') as f:
#     for i in range(0, len(string.ascii_uppercase), letters_per_line):
#         f.write(''.join(string.ascii_uppercase[i:i+letters_per_line]) + '\n')
