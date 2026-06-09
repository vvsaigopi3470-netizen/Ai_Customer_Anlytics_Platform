import joblib

print(
    joblib.load(
        "trained_models/kmeans.pkl"
    )
)

print(
    joblib.load(
        "trained_models/churn_model.pkl"
    )
)

print(
    joblib.load(
        "trained_models/purchase_model.pkl"
    )
)

print(
    "All Models Loaded Successfully"
)