import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset

df=pd.read_excel("Data.xlsx")
print(df.head())        # Display First Five Row
# print(df)

# Create a New columns: TotalRevenue

df["TotalRevenue"]=df['UnitPrice']*df['Quantity'] 

#Save  updated data back to Excel
df.to_excel("Data.xlsx",index=False)

# Total Revenue (All Products)
total_Revenue=np.sum(df["TotalRevenue"])
print(total_Revenue)

# Best Product by Revenue

grouped = df.groupby("ProductName")["TotalRevenue"].max()
best_product = df.groupby("ProductName")["TotalRevenue"].sum().idxmax()
product_revenue = df.groupby("ProductName")["TotalRevenue"].sum().max()
print(f"\n Best Product By Revenue is {best_product } : {product_revenue}")


# Best Category by Revenue

grouped2= df.groupby("ProductCategory")["TotalRevenue"].max()
category=df.groupby("ProductCategory")["TotalRevenue"].sum().idxmax()
product_reven=df.groupby("ProductCategory")["TotalRevenue"].sum().max()
print(f"\n Category Contribute Most Revenue is {category}:{product_reven}")

# Average Order Revenue
average_order_revenue= df.groupby("OrderID")["TotalRevenue"].sum().mean()
print(f"\n Average Order  Revenue: {average_order_revenue}")

# --- Visualization ---

# Revenue by Product (Bar Chart)

product_revenue = df.groupby("ProductName")["TotalRevenue"].sum()
plt.figure(figsize=(11,6))
plt.bar(product_revenue.index,product_revenue.values)
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.show()

# OrderID vs Revenue (Line Chart)
product_order = df.groupby("OrderID")["TotalRevenue"].sum()
plt.figure(figsize=(8,6))
plt.plot(product_order.index,product_order.values,marker="o", linestyle="-",color="b")
plt.figure(figsize=(11,6))
plt.xlabel("Order ID")
plt.ylabel("Revenue")
plt.title("OrderID VS Revenue")
plt.tight_layout()
plt.show()


