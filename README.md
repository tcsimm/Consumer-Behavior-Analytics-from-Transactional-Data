**Consumer Behavior Analytics from Transactional Data**

This project explores and analyzes transactional data from a cafe to uncover patterns in consumer behavior, product popularity, payment methods, and overall spending trends.

**Objectives**
- Clean and prepare raw transaction data for analysis
- Identify high-level trends through exploratory data analysis (EDA)
- Engineer meaningful features for modeling
- Build predictive models for customer spending
- Visualize consumer behavior insights
- Use SQL queries for structured insights

**Project Structure**
- 01_data_cleaning.ipynb	Cleans and preprocesses the raw CSV file
- 02_EDA.ipynb	Summarizes and explores the cleaned data
- 03_feature_engineering.ipynb	Builds new features such as per-item spend and time-based attributes
- 04_modeling.ipynb	Trains regression models to predict total transaction spend
- 05_visualizations.ipynb	Visualizes item popularity, payment methods, and revenue patterns
- 06_sql_analysis.ipynb	Performs SQL-style queries on the dataset using SQLite

Data Files
- dirty_cafe_sales.csv	Raw transaction data
- dirty_cafe_sales_cleaned.csv	Cleaned version used in analysis
- df_encoded.csv	Final modeling-ready dataset with features and encodings

Technologies/tools Used
- Python (Pandas, NumPy, Scikit-learn, Seaborn, SQLite)
- Jupyter Notebooks
- Matplotlib / Seaborn / Plotly (for visualization)
- SQL (via sqlite3 in Python)
