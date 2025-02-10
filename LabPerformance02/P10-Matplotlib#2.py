# Matplotlib#2: Create a bar chart comparing sales revenue across different regions.

import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West", "Central"]
sales_revenue = [90, 50, 65, 99, 62]  

plt.figure(figsize=(8, 5))  
plt.bar(regions, sales_revenue, color=['blue', 'green', 'red', 'purple', 'orange'])

plt.xlabel("regions")
plt.ylabel("sales revenue ($1000s)")
plt.title("sales revenue comparison across regions")

for i, value in enumerate(sales_revenue):
    plt.text(i, value + 2, str(value), ha='center', fontsize=10)

plt.grid(axis='y', linestyle="--", alpha=0.6)

plt.show()
