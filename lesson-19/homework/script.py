#Homework 1

import pandas as pd

# Load sales data
sales_df = pd.read_csv('task/sales_data.csv')

# 1️⃣ Group by Category: total quantity, average price, max quantity in one transaction
category_stats = sales_df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity_transaction=('Quantity', 'max')
).reset_index()

# 2️⃣ Top-selling product in each category
top_products = (sales_df.groupby(['Category', 'Product'])['Quantity']
                .sum()
                .reset_index()
                .sort_values(['Category', 'Quantity'], ascending=[True, False])
                .groupby('Category')
                .first()
                .reset_index())

# 3️⃣ Date with highest total sales
sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']
highest_sales_date = (sales_df.groupby('Date')['Total_Sales']
                      .sum()
                      .reset_index()
                      .sort_values('Total_Sales', ascending=False)
                      .head(1))

print("📊 Category Stats:\n", category_stats)
print("\n🏆 Top Product per Category:\n", top_products)
print("\n📅 Date with Highest Total Sales:\n", highest_sales_date)

#Homework 2

# Load customer orders
orders_df = pd.read_csv('task/customer_orders.csv')

# 1️⃣ Customers with >= 20 orders
orders_per_customer = orders_df.groupby('CustomerID').size().reset_index(name='order_count')
customers_20plus = orders_per_customer[orders_per_customer['order_count'] >= 20]

# 2️⃣ Customers with avg price > $120
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
customers_avg_price_120plus = avg_price_per_customer[avg_price_per_customer['Price'] > 120]

# 3️⃣ Total qty & total price per product, filter qty >= 5
product_totals = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
).reset_index()
products_5plus = product_totals[product_totals['total_quantity'] >= 5]

print("👥 Customers with >=20 orders:\n", customers_20plus)
print("\n💰 Customers with Avg Price > $120:\n", customers_avg_price_120plus)
print("\n📦 Products with Qty >= 5:\n", products_5plus)

#Homework 3
import sqlite3
import numpy as np

# Read population table from DB
conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# Load salary bands
salary_bands = pd.read_excel("task/population salary analysis.xlsx")

# Merge population data with salary bands
merged_df = pd.merge(
    population_df,
    salary_bands,
    how='left',
    left_on='Salary',
    right_on='Salary'
)

# 1️⃣ Measures per salary category
salary_cat_stats = merged_df.groupby('Salary_Category').agg(
    percentage_population=('Salary', lambda x: 100 * len(x) / len(merged_df)),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    count_population=('Salary', 'size')
).reset_index()

# 2️⃣ Measures per salary category *per state*
state_cat_stats = merged_df.groupby(['State', 'Salary_Category']).agg(
    percentage_population=('Salary', lambda x: 100 * len(x) / len(merged_df[merged_df['State'] == x.name[0]])),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    count_population=('Salary', 'size')
).reset_index()

print("📊 Salary Category Stats:\n", salary_cat_stats)
print("\n🏛 State-wise Salary Category Stats:\n", state_cat_stats)


