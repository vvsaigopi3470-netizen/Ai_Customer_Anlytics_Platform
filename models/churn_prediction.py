# models/churn_prediction.py

import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


MODEL_PATH = (
    "trained_models/churn_model.pkl"
)


def train_churn_model(df):

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount",
        "Revenue"
    ]

    X = df[features]

    y = df["Churn"]

    X_train, X_test, y_train, y_test = \
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"Churn Accuracy: {accuracy:.2f}"
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


def predict_churn_customers(df):

    if not os.path.exists(MODEL_PATH):
        train_churn_model(df)

    model = joblib.load(
        MODEL_PATH
    )

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount",
        "Revenue"
    ]

    X = df[features]

    predictions = model.predict(X)

    probabilities = model.predict_proba(
        X
    )[:, 1]

    results = []

    for i in range(len(df)):

        results.append({

            "CustomerID":
                int(
                    df.iloc[i]["CustomerID"]
                ),

            "Prediction":
                "Likely To Leave"
                if predictions[i] == 1
                else "Active",

            "Probability":
                round(
                    probabilities[i] * 100,
                    2
                )
        })

    return results


def predict_single_customer(data):

    model = joblib.load(
        MODEL_PATH
    )

    prediction = model.predict(
        [data]
    )

    probability = model.predict_proba(
        [data]
    )[0][1]

    return {

        "prediction":
            int(prediction[0]),

        "probability":
            round(
                probability * 100,
                2
            )
    }