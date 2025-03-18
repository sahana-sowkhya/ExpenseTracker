# Analyzing Personal Expenses

## Overview
This project simulates an expense tracker for an individual by generating realistic monthly expense data using the Faker library. The data is processed and stored in an SQLite database, queried using SQL, and visualized via a Streamlit dashboard. The project provides insights into spending habits across various categories and payment modes, helping users understand and optimize their personal finances.

## Skills & Technologies
- **Python:** Data simulation, SQL integration, and exploratory data analysis (EDA)
- **SQL:** Creating a database schema, loading data, and executing queries
- **Streamlit:** Developing an interactive web application for data visualization
- **Faker:** Generating realistic expense data

## Problem Statement
The project simulates a personal expense tracker by:
- Generating monthly expense data (for 12 months) with realistic attributes such as date, category, payment mode, description, amount paid, and cashback.
- Storing the generated data in an SQLite database.
- Executing SQL queries to derive insights such as total spending per category, spending by payment mode, cashback earned, recurring expenses, and more.
- Visualizing the results using a user-friendly Streamlit dashboard.

## Business Use Cases
- **Automated Expense Tracking:** Automatically track personal or business expenses.
- **Spending Analysis:** Categorize spending habits to create actionable savings plans.
- **Dashboard Reporting:** Build financial dashboards to monitor income and expenditure trends.
- **Procurement Insights:** Provide insights into purchasing patterns for improved financial management.

## Project Structure
```
ExpenseTracker/
├── env/                    # Virtual environment (created locally)
├── expenses_01.csv         # Simulated data for January (and similarly for other months)
├── expenses_02.csv
├── ... (up to expenses_12.csv)
├── expenses.db             # SQLite database (created by load_data.py)
├── simulate_data.py        # Script to generate simulated expense data using Faker
├── load_data.py            # Script to load CSV files into the SQLite database
├── app.py                  # Streamlit app displaying SQL query outputs and visualizations
└── README.md               # This documentation file
```

## Setup & Installation

1. **Set Up the Virtual Environment** (optional but recommended)
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. **Install Required Packages**
   ```bash
   pip install Faker pandas sqlalchemy streamlit matplotlib
   ```

3. **Generate Expense Data**
   Run the simulation script to create CSV files for each month:
   ```bash
   python3 simulate_data.py
   ```
   This will generate 12 CSV files (`expenses_01.csv` through `expenses_12.csv`).

4. **Load Data into the Database**
   Run the load data script:
   ```bash
   python load_data.py
   ```
   This will create/update the `expenses.db` with data loaded into a table named `expenses`.

5. **Launch the Streamlit Dashboard**
   Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   Your browser will open the dashboard, displaying insights like total spending by category, payment mode, cashback, and more.

## SQL Queries & Analysis
The Streamlit app integrates 15 SQL queries addressing the following:
1. Total amount spent in each category.
2. Total amount spent using each payment mode.
3. Total cashback received.
4. Top 5 most expensive categories.
5. Transportation spending by payment mode.
6. Transactions with cashback.
7. Total spending per month.
8. Monthly spending for categories like Travel, Entertainment, or Gifts.
9. Recurring expenses across months.
10. Monthly cashback earned.
11. Overall spending trend over time.
12. Typical travel costs (analyzed by description).
13. Grocery spending patterns by weekday.
14. High vs. low priority expense categories.
15. Category contributing the highest percentage of total spending.

## Screenshots

![Screenshot 2025-03-18 at 10.35.27 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.27%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.35.35 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.35%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.35.45 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.45%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.35.51 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.51%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.35.55 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.55%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.35.59 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.35.59%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.36.04 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.36.04%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.36.09 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.36.09%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.36.13 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.36.13%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.36.17 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.36.17%E2%80%AFPM.png)
![Screenshot 2025-03-18 at 10.36.23 PM.png](Screenshot-ExpenseTracker/Screenshot%202025-03-18%20at%2010.36.23%E2%80%AFPM.png)


## Conclusion
This project demonstrates how to simulate, process, and analyze personal expense data using Python, SQL, and Streamlit. The interactive dashboard provides a comprehensive view of spending habits and actionable insights to help manage finances effectively.

## References
- [Faker Library Documentation](https://faker.readthedocs.io/en/master/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Python Official Documentation](https://docs.python.org/3/)
