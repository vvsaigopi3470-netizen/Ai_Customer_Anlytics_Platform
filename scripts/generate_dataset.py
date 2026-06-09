import pandas as pd
import numpy as np
import random
import os

os.makedirs("dataset", exist_ok=True)

records = []

for customer_id in range(1, 501):

    gender = random.choice(
        ["Male", "Female"]
    )

    age = random.randint(
        18,
        70
    )

    income = random.randint(
        20000,
        150000
    )

    spending_score = random.randint(
        1,
        100
    )

    purchase_count = random.randint(
        1,
        30
    )

    revenue = (
        spending_score *
        purchase_count *
        random.randint(50, 150)
    )

    churn = 1 if (
        spending_score < 30 and
        purchase_count < 5
    ) else 0

    records.append([
        customer_id,
        gender,
        age,
        income,
        spending_score,
        purchase_count,
        revenue,
        churn
    ])

df = pd.DataFrame(
    records,
    columns=[
        "CustomerID",
        "Gender",
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount",
        "Revenue",
        "Churn"
    ]
)

df.to_csv(
    "dataset/customer_data.csv",
    index=False
)

print("Dataset Generated Successfully")
print(df.head())