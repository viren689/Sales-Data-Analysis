# Week 3 - Sales Data Analysis
# Import pandas library

import os
import pandas as pd

# Read the CSV
df = pd.read_csv("sales_data.csv")

print("=" * 50)
print("SALES DATA ANALYSIS")
print("=" * 50)

# Display first five rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Calculate missing Total_Sales
df["Total_Sales"] = df["Total_Sales"].fillna(df["Quantity"] * df["Price"])

# Remove duplicate rows
df = df.drop_duplicates()

# Calculate metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

# Best selling product
best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

print("\n" + "=" * 50)
print("SALES REPORT")
print("=" * 50)

print(f"Total Revenue : ₹{total_sales:,.2f}")
print(f"Average Sale  : ₹{average_sales:,.2f}")
print(f"Highest Sale  : ₹{highest_sale:,.2f}")
print(f"Lowest Sale   : ₹{lowest_sale:,.2f}")
print(f"Best Product  : {best_product}")

print("\nAnalysis Completed Successfully!")
