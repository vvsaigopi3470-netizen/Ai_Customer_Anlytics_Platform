import pandas as pd

from models.churn_prediction import (
    train_churn_model
)

df = pd.read_csv(
    "dataset/customer_data.csv"
)

train_churn_model(df)

print(
    "Churn Model Trained"
)