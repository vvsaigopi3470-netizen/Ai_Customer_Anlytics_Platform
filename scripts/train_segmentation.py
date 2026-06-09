import pandas as pd

from models.segmentation import (
    train_segmentation_model
)

df = pd.read_csv(
    "dataset/customer_data.csv"
)

train_segmentation_model(df)

print(
    "Segmentation Model Trained"
)