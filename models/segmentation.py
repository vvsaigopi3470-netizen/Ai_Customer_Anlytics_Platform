# models/segmentation.py

import os
import joblib
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


MODEL_PATH = "trained_models/kmeans.pkl"
SCALER_PATH = "trained_models/segment_scaler.pkl"


def train_segmentation_model(df):

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount",
        "Revenue"
    ]

    X = df[features]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    os.makedirs(
        "trained_models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        scaler,
        SCALER_PATH
    )

    return model


def perform_segmentation(df):

    if not os.path.exists(MODEL_PATH):
        train_segmentation_model(df)

    model = joblib.load(
        MODEL_PATH
    )

    scaler = joblib.load(
        SCALER_PATH
    )

    features = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseCount",
        "Revenue"
    ]

    X = df[features]

    X_scaled = scaler.transform(X)

    clusters = model.predict(
        X_scaled
    )

    segmented_df = df.copy()

    segmented_df["Segment"] = clusters

    return segmented_df