# Pandas#1: Load a CSV file of sales data and compute total revenue per product.

import pandas as pd

df = pd.read_csv("D:\code\Artificial-Intelligence-Lab\LabPerformance02\Sales_Data.csv");

df['Revenue'] = df['Quantity'] * df['Price']
TR = df.groupby('Product')['Revenue'].sum().reset_index()
print(TR)
