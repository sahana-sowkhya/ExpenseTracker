# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

st.title("Expense Tracker Dashboard")

# Connect to the SQLite database
engine = create_engine('sqlite:///expenses.db')

# Load complete expense data
df = pd.read_sql("SELECT * FROM expenses", con=engine)
st.header("Expense Data Overview")
st.write("First 10 records:")
st.dataframe(df.head(10))

# 1. Total amount spent in each category
st.header("1. Total Amount Spent in Each Category")
query1 = """
SELECT Category, SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Category;
"""
df1 = pd.read_sql(query1, con=engine)
st.table(df1)

# 2. Total amount spent using each payment mode
st.header("2. Total Amount Spent Using Each Payment Mode")
query2 = """
SELECT Payment_Mode, SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Payment_Mode;
"""
df2 = pd.read_sql(query2, con=engine)
st.table(df2)

# 3. Total cashback received across all transactions
st.header("3. Total Cashback Received")
query3 = """
SELECT SUM(Cashback) AS Total_Cashback
FROM expenses;
"""
df3 = pd.read_sql(query3, con=engine)
st.write(f"${df3.iloc[0, 0]:,.2f}")

# 4. Top 5 most expensive categories in terms of spending
st.header("4. Top 5 Most Expensive Categories")
query4 = """
SELECT Category, SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Category
ORDER BY Total_Spent DESC
LIMIT 5;
"""
df4 = pd.read_sql(query4, con=engine)
st.table(df4)

# 5. How much was spent on transportation using different payment modes
st.header("5. Transportation Spending by Payment Mode")
query5 = """
SELECT Payment_Mode, SUM(Amount_Paid) AS Total_Spent
FROM expenses
WHERE Category = 'Transportation'
GROUP BY Payment_Mode;
"""
df5 = pd.read_sql(query5, con=engine)
st.table(df5)

# 6. Which transactions resulted in cashback
st.header("6. Transactions with Cashback")
query6 = """
SELECT *
FROM expenses
WHERE Cashback > 0;
"""
df6 = pd.read_sql(query6, con=engine)
st.dataframe(df6)

# 7. What is the total spending in each month of the year
st.header("7. Total Spending Per Month")
query7 = """
SELECT Month, SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Month
ORDER BY Month;
"""
df7 = pd.read_sql(query7, con=engine)
st.table(df7)

# 8. Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"
st.header("8. Monthly Spending for Travel, Entertainment, or Gifts")
query8 = """
SELECT Month, Category, SUM(Amount_Paid) AS Total_Spent
FROM expenses
WHERE Category IN ('Travel', 'Entertainment', 'Gifts')
GROUP BY Month, Category
ORDER BY Total_Spent DESC;
"""
df8 = pd.read_sql(query8, con=engine)
st.table(df8)

# 9. Recurring expenses that occur during specific months (e.g., insurance premiums, property taxes)
st.header("9. Recurring Expenses by Month")
query9 = """
SELECT Description, COUNT(*) AS Occurrences, GROUP_CONCAT(DISTINCT Month) AS Months
FROM expenses
GROUP BY Description
HAVING Occurrences > 1;
"""
df9 = pd.read_sql(query9, con=engine)
st.table(df9)

# 10. How much cashback or rewards were earned in each month
st.header("10. Monthly Cashback Earned")
query10 = """
SELECT Month, SUM(Cashback) AS Total_Cashback
FROM expenses
GROUP BY Month
ORDER BY Month;
"""
df10 = pd.read_sql(query10, con=engine)
st.table(df10)

# 11. How has your overall spending changed over time (spending trend)
st.header("11. Overall Spending Trend Over Time")
query11 = """
SELECT Month, SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Month
ORDER BY Month;
"""
df11 = pd.read_sql(query11, con=engine)
st.table(df11)
# Plot spending trend
fig, ax = plt.subplots()
ax.plot(df11['Month'], df11['Total_Spent'], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Total Spending")
ax.set_title("Overall Spending Trend")
st.pyplot(fig)

# 12. Typical costs associated with different types of travel
st.header("12. Typical Travel Costs")
query12 = """
SELECT Description, AVG(Amount_Paid) AS Avg_Cost, COUNT(*) AS Frequency
FROM expenses
WHERE Category = 'Travel'
GROUP BY Description
ORDER BY Avg_Cost DESC;
"""
df12 = pd.read_sql(query12, con=engine)
st.table(df12)

# 13. Patterns in grocery spending (e.g., spending on weekends)
st.header("13. Grocery Spending Patterns by Weekday")
query13 = """
SELECT strftime('%w', Date) AS Weekday, SUM(Amount_Paid) AS Total_Spent
FROM expenses
WHERE Category = 'Groceries'
GROUP BY Weekday
ORDER BY Weekday;
"""
df13 = pd.read_sql(query13, con=engine)
st.table(df13)

# 14. Define High and Low Priority Categories
st.header("14. High vs. Low Priority Categories")
query14 = """
SELECT 
  CASE 
    WHEN Category IN ('Bills', 'Groceries') THEN 'High Priority'
    ELSE 'Low Priority'
  END AS Priority,
  SUM(Amount_Paid) AS Total_Spent
FROM expenses
GROUP BY Priority;
"""
df14 = pd.read_sql(query14, con=engine)
st.table(df14)

# 15. Which category contributes the highest percentage of the total spending?
st.header("15. Category with the Highest Percentage of Total Spending")
query15 = """
SELECT Category,
       (SUM(Amount_Paid) * 100.0 / (SELECT SUM(Amount_Paid) FROM expenses)) AS Percentage
FROM expenses
GROUP BY Category
ORDER BY Percentage DESC
LIMIT 1;
"""
df15 = pd.read_sql(query15, con=engine)
st.table(df15)

