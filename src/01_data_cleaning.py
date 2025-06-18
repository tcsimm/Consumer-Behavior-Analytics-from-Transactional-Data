# 1 - data cleaning

# Import libraries
import pandas as pd

# Load raw dataset
df = pd.read_csv("dirty_cafe_sales.csv")

# Drop duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Handle missing values (basic example)
df = df.dropna(subset=['Transaction_ID', 'Item', 'Price_Per_Unit', 'Quantity'])

# Fix data types
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price_Per_Unit'] = pd.to_numeric(df['Price_Per_Unit'], errors='coerce')
df['Total_Spent'] = df['Quantity'] * df['Price_Per_Unit']

# Create month column
df['Month'] = df['Transaction_Date'].dt.to_period('M').astype(str)

# Sort by date
df = df.sort_values('Transaction_Date')

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("dirty_cafe_sales_cleaned.csv", index=False)
