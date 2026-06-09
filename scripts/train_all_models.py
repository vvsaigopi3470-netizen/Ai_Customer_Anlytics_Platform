import os
import sys
import pandas as pd

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from models.segmentation import (
    train_segmentation_model
)

from models.churn_prediction import (
    train_churn_model
)

from models.purchase_prediction import (
    train_purchase_model
)

print(
    "Loading Dataset..."
)

df = pd.read_csv(
    "dataset/customer_data.csv"
)

print(
    "Training Segmentation Model..."
)

train_segmentation_model(df)

print(
    "Training Churn Model..."
)

train_churn_model(df)

print(
    "Training Purchase Model..."
)

train_purchase_model(df)

print(
    "\nAll Models Trained Successfully"
)