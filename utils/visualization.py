# utils/visualization.py

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

UPLOAD_FOLDER = "static/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# =====================================
# REVENUE BAR CHART
# =====================================

def create_revenue_chart(df):

    if "Revenue" not in df.columns:
        return "<h3>No Revenue Data Available</h3>"

    revenue_df = df.sort_values(
        by="Revenue",
        ascending=False
    ).head(20)

    fig = px.bar(
        revenue_df,
        x="CustomerID",
        y="Revenue",
        title="Top 20 Revenue Generating Customers",
        text="Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# AGE DISTRIBUTION
# =====================================

def create_age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=15,
        title="Customer Age Distribution"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# INCOME VS SPENDING
# =====================================

def create_income_spending_chart(df):

    fig = px.scatter(
        df,
        x="AnnualIncome",
        y="SpendingScore",
        color="Gender",
        title="Income vs Spending Score",
        hover_data=["CustomerID"]
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# CHURN PIE CHART
# =====================================

def create_churn_chart(df):

    if "Churn" not in df.columns:
        return "<h3>No Churn Data Available</h3>"

    churn_counts = (
        df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn_counts.columns = [
        "Status",
        "Count"
    ]

    churn_counts["Status"] = (
        churn_counts["Status"]
        .map({
            0: "Active",
            1: "Churned"
        })
    )

    fig = px.pie(
        churn_counts,
        names="Status",
        values="Count",
        title="Customer Churn Analysis"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# REVENUE DISTRIBUTION
# =====================================

def create_revenue_distribution(df):

    fig = px.histogram(
        df,
        x="Revenue",
        nbins=20,
        title="Revenue Distribution"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# PURCHASE COUNT ANALYSIS
# =====================================

def create_purchase_chart(df):

    fig = px.box(
        df,
        y="PurchaseCount",
        title="Purchase Count Analysis"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# SEGMENTATION PLOT
# =====================================

def create_segment_chart(df):

    if "Segment" not in df.columns:
        return None

    plt.figure(
        figsize=(10, 6)
    )

    scatter = plt.scatter(
        df["AnnualIncome"],
        df["SpendingScore"],
        c=df["Segment"]
    )

    plt.xlabel(
        "Annual Income"
    )

    plt.ylabel(
        "Spending Score"
    )

    plt.title(
        "Customer Segmentation"
    )

    plt.colorbar(
        scatter
    )

    image_path = os.path.join(
        UPLOAD_FOLDER,
        "segment_plot.png"
    )

    plt.savefig(
        image_path,
        bbox_inches="tight"
    )

    plt.close()

    return image_path


# =====================================
# SEGMENT WISE REVENUE
# =====================================

def create_segment_revenue_chart(df):

    if "Segment" not in df.columns:
        return "<h3>No Segment Data</h3>"

    segment_df = (
        df.groupby("Segment")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        segment_df,
        x="Segment",
        y="Revenue",
        title="Revenue By Customer Segment"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# CUSTOMER RETENTION CHART
# =====================================

def create_retention_chart(df):

    retained = len(
        df[df["Churn"] == 0]
    )

    churned = len(
        df[df["Churn"] == 1]
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["Retained"],
            y=[retained],
            name="Retained"
        )
    )

    fig.add_trace(
        go.Bar(
            x=["Churned"],
            y=[churned],
            name="Churned"
        )
    )

    fig.update_layout(
        title="Customer Retention Analysis"
    )

    return fig.to_html(
        full_html=False
    )


# =====================================
# KPI METRICS
# =====================================

def dashboard_metrics(df):

    metrics = {

        "Total Customers":
        len(df),

        "Total Revenue":
        round(
            df["Revenue"].sum(),
            2
        ),

        "Average Revenue":
        round(
            df["Revenue"].mean(),
            2
        ),

        "Average Age":
        round(
            df["Age"].mean(),
            2
        ),

        "Average Spending":
        round(
            df["SpendingScore"].mean(),
            2
        ),

        "Total Purchases":
        int(
            df["PurchaseCount"].sum()
        ),

        "Churn Customers":
        int(
            df["Churn"].sum()
        )
    }

    return metrics


# =====================================
# AI INSIGHTS
# =====================================

def generate_ai_insights(df):

    insights = []

    total_customers = len(df)

    total_revenue = round(
        df["Revenue"].sum(),
        2
    )

    avg_spending = round(
        df["SpendingScore"].mean(),
        2
    )

    churn_count = int(
        df["Churn"].sum()
    )

    churn_rate = round(
        (churn_count / total_customers)
        * 100,
        2
    )

    insights.append(
        f"Total Customers: {total_customers}"
    )

    insights.append(
        f"Total Revenue: ₹{total_revenue}"
    )

    insights.append(
        f"Average Spending Score: {avg_spending}"
    )

    insights.append(
        f"Churn Rate: {churn_rate}%"
    )

    if churn_rate > 20:

        insights.append(
            "High churn risk detected. Retention campaigns recommended."
        )

    else:

        insights.append(
            "Customer retention is healthy."
        )

    high_value = len(
        df[df["SpendingScore"] > 75]
    )

    insights.append(
        f"{high_value} customers are classified as premium customers."
    )

    return insights


# =====================================
# CUSTOMER SUMMARY
# =====================================

def customer_summary(df):

    summary = {

        "rows":
        df.shape[0],

        "columns":
        df.shape[1],

        "missing_values":
        int(
            df.isnull()
            .sum()
            .sum()
        ),

        "duplicates":
        int(
            df.duplicated()
            .sum()
        )
    }

    return summary