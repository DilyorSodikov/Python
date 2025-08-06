import pandas as pd
import numpy as np
#Homework 1
# Create the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename columns using function
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# 2. Print first 3 rows
print("First 3 rows:")
print(df.head(3), "\n")

# 3. Mean age
mean_age = df['age'].mean()
print("Mean age:", mean_age, "\n")

# 4. Select and print only 'first_name' and 'city' columns
print("Name and City columns:")
print(df[['first_name', 'city']], "\n")

# 5. Add new column 'Salary' with random salary values
df['salary'] = np.random.randint(40000, 80000, size=len(df))
print("DataFrame with Salary column:")
print(df, "\n")

# 6. Display summary statistics
print("Summary statistics:")
print(df.describe(include='all'))

#Homework 2
# 1. Create DataFrame
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

# 2. Maximum sales and expenses
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max(), "\n")

# 3. Minimum sales and expenses
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min(), "\n")

# 4. Average sales and expenses
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean(), "\n")

#Homework 3
# 1. Create DataFrame
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)

# Set 'Category' as index
expenses = expenses.set_index('Category')

# 2. Max expense per category
print("Maximum expense per category:")
print(expenses.max(axis=1), "\n")

# 3. Minimum expense per category
print("Minimum expense per category:")
print(expenses.min(axis=1), "\n")

# 4. Average expense per category
print("Average expense per category:")
print(expenses.mean(axis=1), "\n")
