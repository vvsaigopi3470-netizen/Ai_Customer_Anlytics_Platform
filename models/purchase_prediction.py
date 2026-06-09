# models/purchase_prediction.py

import os
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


MODEL_PATH = (
    "trained_models/purchase_model.pkl"
)


def train_purchase_model(df):

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount"
    ]

    X = df[features]

    y = df["Revenue"]

    X_train, X_test, y_train, y_test = \
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    score = r2_score(
        y_test,
        predictions
    )

    print(
        f"Purchase Model R2: {score:.2f}"
    )

    os.makedirs(
        "trained_models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    return model


def predict_purchase_value(
    spending_score
):

    """
    Simple prediction
    based on spending score
    """

    return round(
        spending_score * 150,
        2
    )


def predict_customer_revenue(
    age,
    income,
    spending_score,
    purchase_count
):

    model = joblib.load(
        MODEL_PATH
    )

    prediction = model.predict(
        [[
            age,
            income,
            spending_score,
            purchase_count
        ]]
    )

    return round(
        float(prediction[0]),
        2
    )