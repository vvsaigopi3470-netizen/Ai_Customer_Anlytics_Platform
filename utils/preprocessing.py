import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


def load_dataset(filepath):

    return pd.read_csv(filepath)


def clean_data(df):

    df = df.copy()

    df.drop_duplicates(
        inplace=True
    )

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    categorical_cols = df.select_dtypes(
        include='object'
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].mean()
        )

    for col in categorical_cols:

        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    return df


def encode_data(df):

    df = df.copy()

    encoder = LabelEncoder()

    categorical_cols = df.select_dtypes(
        include='object'
    ).columns

    for col in categorical_cols:

        df[col] = encoder.fit_transform(
            df[col]
        )

    return df


def scale_features(df):

    df = df.copy()

    scaler = StandardScaler()

    numeric_cols = [

        col for col in df.columns

        if col != "CustomerID"
    ]

    df[numeric_cols] = scaler.fit_transform(
        df[numeric_cols]
    )

    return df


def preprocess_dataset(df):

    df = clean_data(df)

    df = encode_data(df)

    return df


def dataset_summary(df):

    return {

        "Rows":
        int(df.shape[0]),

        "Columns":
        int(df.shape[1]),

        "Missing Values":
        int(df.isnull().sum().sum()),

        "Duplicate Records":
        int(df.duplicated().sum())
    }