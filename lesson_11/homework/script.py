# # Homework:

# # Create your own virtual environment and install some python packages.
# # Create custom modules.
# # Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
# # Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
# # Create custom packages.
# # Create geometry package.
# #  geometry\
# #      __init__.py
# #      circle.py
 
# # Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
# # Create file_operations package.
# #  file_operations\
# #      __init__.py
# #      file_reader.py
# #      file_writer.py
 
# # Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).

# # main.py

# # --- Custom Modules ---
# from math_operations import add, subtract, multiply, divide
# from string_utils import reverse_string, count_vowels

# # --- Custom Packages ---
# from geometry import calculate_area, calculate_circumference
# from file_operations import write_file, read_file

# def test_math_operations():
#     print("=== Math Operations ===")
#     print("Add: 5 + 3 =", add(5, 3))
#     print("Subtract: 10 - 4 =", subtract(10, 4))
#     print("Multiply: 7 * 6 =", multiply(7, 6))
#     print("Divide: 8 / 2 =", divide(8, 2))
#     print()

# def test_string_utils():
#     print("=== String Utilities ===")
#     s = "Hello World"
#     print("Original:", s)
#     print("Reversed:", reverse_string(s))
#     print("Vowels count:", count_vowels(s))
#     print()

# def test_geometry():
#     print("=== Geometry (Circle) ===")
#     radius = 5
#     print("Radius:", radius)
#     print("Area:", calculate_area(radius))
#     print("Circumference:", calculate_circumference(radius))
#     print()

# def test_file_operations():
#     print("=== File Operations ===")
#     path = "sample.txt"
#     content = "This is a sample file.\nCreated with custom package."
#     write_file(path, content)
#     print("Written content:")
#     print(read_file(path))
#     print()

# if __name__ == "__main__":
#     test_math_operations()
#     test_string_utils()
#     test_geometry()
#     test_file_operations()
