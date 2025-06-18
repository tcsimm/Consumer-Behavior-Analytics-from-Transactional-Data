# 2 - EDA

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read cleaned csv file
df = pd.read_csv("/Users/thomassimmons/c/td/data/dirty_cafe_sales_cleaned.csv")

# Start out with summary statistics
df.describe()
df.info()
df.isnull().sum()

# Distributions of items
sns.histplot(df['Item'], kde=False)
plt.title("Distribution of Items")
plt.show()

# Correlations
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Total spent distribution
sns.histplot(df['Total Spent'], bins=30, kde=True)
plt.title("Distribution of Total Spent per Transaction")
plt.show()

# Revenue by location
revenue_by_location = df.groupby('Location')['Total Spent'].sum().sort_values()
revenue_by_location.plot(kind='bar', title='Revenue by Location')
plt.ylabel("Revenue Amount")
plt.show()

# Payment method distribution
sns.countplot(data=df, y='Payment Method', order=df['Payment Method'].value_counts().index)
plt.title("Payment Method Distribution")
plt.show()

# Converting since previous notebook 
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Monthly sales trend
monthly_sales = df.groupby('Month')['Total Spent'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trends")
plt.ylabel("Revenue")
plt.show()

