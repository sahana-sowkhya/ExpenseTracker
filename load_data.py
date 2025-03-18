# load_data.py

import pandas as pd
from sqlalchemy import create_engine

# Create an SQLite engine; the database file will be created as expenses.db
engine = create_engine('sqlite:///expenses.db')

df_list = []
for month in range(1, 13):
    df = pd.read_csv(f"expenses_{month:02d}.csv")
    # Optionally add a Month column for easier querying
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    df_list.append(df)

all_data = pd.concat(df_list, ignore_index=True)

# Load data into the "expenses" table, replacing any existing table
all_data.to_sql('expenses', con=engine, if_exists='replace', index=False)
print("Data loaded successfully into expenses.db")
