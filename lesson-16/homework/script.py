import numpy as np

# 1. Convert List to 1D Array
print("1. Convert List to 1D Array")
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d, "\n")

# 2. Create 3x3 Matrix with values from 2 to 10
print("2. Create 3x3 Matrix (2–10)")
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3, "\n")

# 3. Null Vector (10) & Update Sixth Value
print("3. Null Vector of Size 10 & Update Sixth Value")
null_vector = np.zeros(10)
print("Original null vector:")
print(null_vector)
null_vector[6] = 11
print("After update:")
print(null_vector, "\n")

# 4. Array from 12 to 38
print("4. Array from 12 to 38")
array_12_38 = np.arange(12, 38)
print(array_12_38, "\n")

# 5. Convert Array to Float Type
print("5. Convert Array to Float Type")
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("Original array:", int_array)
print("Float array:", float_array, "\n")

# 6. Celsius to Fahrenheit Conversion
print("6. Celsius to Fahrenheit Conversion")
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.0])
fahrenheit = (celsius * 9 / 5) + 32
print("Values in Centigrade degrees:")
print(celsius)
print("Values in Fahrenheit degrees:")
print(fahrenheit, "\n")

# 7. Append Values to Array
print("7. Append Values to Array")
original_array = np.array([10, 20, 30])
values_to_append = [40, 50, 60, 70, 80, 90]
appended_array = np.append(original_array, values_to_append)
print("Original array:", original_array)
print("After append values:", appended_array, "\n")

# 8. Array Statistical Functions
print("8. Array Statistical Functions")
random_array = np.random.rand(10)
print("Random array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array), "\n")

# 9. Find Min and Max in 10x10 Array
print("9. Min and Max in 10x10 Array")
array_10x10 = np.random.rand(10, 10)
print("10x10 Random Array:\n", array_10x10)
print("Minimum value:", np.min(array_10x10))
print("Maximum value:", np.max(array_10x10), "\n")

# 10. 3x3x3 Array with Random Values
print("10. 3x3x3 Array with Random Values")
array_3x3x3 = np.random.rand(3, 3, 3)
print(array_3x3x3)
