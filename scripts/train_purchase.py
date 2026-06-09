import pandas as pd

from models.purchase_prediction import (
    train_purchase_model
)

df = pd.read_csv(
    "dataset/customer_data.csv"
)

train_purchase_model(df)

print(
    "Purchase Model Trained"
)