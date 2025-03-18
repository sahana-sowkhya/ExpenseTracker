# simulate_data.py

from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()
categories = ['Food', 'Transportation', 'Bills', 'Groceries', 'Subscriptions', 'Entertainment', 'Travel']
payment_modes = ['Cash', 'Online']

def generate_expense_data(month, year, num_entries=100):
    data = []
    for _ in range(num_entries):
        start_date = datetime(year, month, 1)
        # Using 28 days for simplicity
        end_date = datetime(year, month, 28)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        category = random.choice(categories)
        payment_mode = random.choice(payment_modes)
        description = fake.sentence(nb_words=6)
        amount_paid = round(random.uniform(10, 500), 2)
        # 30% chance to get 5% cashback
        cashback = round(amount_paid * 0.05, 2) if random.random() < 0.3 else 0.0
        data.append({
            'Date': random_date.strftime("%Y-%m-%d"),
            'Category': category,
            'Payment_Mode': payment_mode,
            'Description': description,
            'Amount_Paid': amount_paid,
            'Cashback': cashback
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    for month in range(1, 13):
        df = generate_expense_data(month, 2024, num_entries=100)
        df.to_csv(f"expenses_{month:02d}.csv", index=False)
    print("CSV files generated for all 12 months.")
