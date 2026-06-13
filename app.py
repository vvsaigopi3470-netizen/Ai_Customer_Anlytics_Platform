from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

import os
import pandas as pd

# ============================
# Preprocessing
# ============================

from utils.preprocessing import (
    preprocess_dataset
)

# ============================
# Visualization
# ============================

from utils.visualization import (
    create_revenue_chart,
    create_segment_chart,
    dashboard_metrics,
    generate_ai_insights
)

# ============================
# Models
# ============================

from models.segmentation import (
    perform_segmentation
)

from models.churn_prediction import (
    predict_churn_customers
)

from models.purchase_prediction import (
    predict_purchase_value
)

from models.recommendation import (
    recommend_products
)

# ============================
# Flask App
# ============================

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

customer_df = None


def standardize_columns(df):

    df = df.copy()

    column_mapping = {

        "customerid": "CustomerID",
        "customer id": "CustomerID",
        "customer_id": "CustomerID",
        "age": "Age",
        "annualincome": "AnnualIncome",
        "annual income": "AnnualIncome",
        "annual_income": "AnnualIncome",
        "spendingscore": "SpendingScore",
        "spending score": "SpendingScore",
        "spending_score": "SpendingScore",
        "purchasecount": "PurchaseCount",
        "purchase count": "PurchaseCount",
        "purchase_count": "PurchaseCount",
        "revenue": "Revenue",
        "churn": "Churn"
    }

    renamed_columns = {}

    for col in df.columns:

        normalized = col.strip().lower()

        normalized = normalized.replace(" ", "").replace("_", "")

        if normalized in column_mapping:

            renamed_columns[col] = column_mapping[normalized]

        else:

            renamed_columns[col] = col

    return df.rename(columns=renamed_columns)


# ============================
# Home
# ============================

@app.route('/')
def home():

    return render_template(
        'index.html'
    )

# ============================
# Upload Page
# ============================

@app.route('/upload')
def upload():

    return render_template(
        'upload.html'
    )

# ============================
# Upload Dataset
# ============================

@app.route(
    '/upload_dataset',
    methods=['POST']
)
def upload_dataset():

    global customer_df

    if 'file' not in request.files:

        return "No File Uploaded"

    file = request.files['file']

    if file.filename == '':

        return "Please Select a File"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    try:

        # ------------------------
        # Read CSV or Excel
        # ------------------------

        if file.filename.lower().endswith('.csv'):

            customer_df = pd.read_csv(
                filepath
            )

        elif file.filename.lower().endswith('.xlsx'):

            customer_df = pd.read_excel(
                filepath
            )

        else:

            return """
            <h3>
            Only CSV and Excel Files
            Are Supported
            </h3>
            """

        # ------------------------
        # Standardize Columns
        # ------------------------

        customer_df = standardize_columns(
            customer_df
        )

        # ------------------------
        # Create Missing Columns
        # ------------------------

        required_columns = [

            "CustomerID",
            "Age",
            "AnnualIncome",
            "SpendingScore",
            "PurchaseCount",
            "Revenue",
            "Churn"
        ]

        for col in required_columns:

            if col not in customer_df.columns:

                if col == "CustomerID":

                    customer_df[col] = range(
                        1,
                        len(customer_df) + 1
                    )

                elif col == "Age":

                    customer_df[col] = 30

                elif col == "AnnualIncome":

                    customer_df[col] = 50000

                elif col == "SpendingScore":

                    customer_df[col] = 50

                elif col == "PurchaseCount":

                    customer_df[col] = 5

                elif col == "Revenue":

                    customer_df[col] = 10000

                elif col == "Churn":

                    customer_df[col] = 0

        # ------------------------
        # Handle Missing Values
        # ------------------------

        customer_df.fillna(
            0,
            inplace=True
        )

        # ------------------------
        # Preprocess Dataset
        # ------------------------

        customer_df = preprocess_dataset(
            customer_df
        )

        return redirect(
            url_for('dashboard')
        )

    except Exception as e:

        return f"""
        <h3>
        Dataset Upload Failed
        </h3>

        <p>
        {str(e)}
        </p>
        """
    
        # ============================
        # Dynamic Column Mapping
        # ============================

def standardize_columns(df):
    column_mapping = {
        # Customer ID
        "customerid": "CustomerID",
        "customer_id": "CustomerID",
        "id": "CustomerID",

        # Age
        "age": "Age",

        # Income
        "annualincome": "AnnualIncome",
        "annual_income": "AnnualIncome",
        "income": "AnnualIncome",
        "salary": "AnnualIncome",

        # Spending Score
        "spendingscore": "SpendingScore",
        "spending_score": "SpendingScore",
        "score": "SpendingScore",
        "spending": "SpendingScore",

        # Purchase Count
        "purchasecount": "PurchaseCount",
        "purchase_count": "PurchaseCount",
        "orders": "PurchaseCount",
        "purchases": "PurchaseCount",
        "transactions": "PurchaseCount",

        # Revenue
        "revenue": "Revenue",
        "sales": "Revenue",
        "amountspent": "Revenue",
        "amount_spent": "Revenue",
        "totalspend": "Revenue",

        # Churn
        "churn": "Churn",
        "left": "Churn",
        "exited": "Churn"
    }

    rename_dict = {}
    for col in df.columns:
        clean_col = (
            col.lower()
            .replace(" ", "")
            .replace("-", "")
            .replace("_", "")
        )
        if clean_col in column_mapping:
            rename_dict[col] = column_mapping[clean_col]

    df.rename(columns=rename_dict, inplace=True)
    return df
    
# ============================
# Dashboard
# ============================

@app.route('/dashboard')
def dashboard():

    global customer_df

    if customer_df is None:

        return redirect(
            url_for('home')
        )

    metrics = dashboard_metrics(
        customer_df
    )

    insights = generate_ai_insights(
        customer_df
    )

    revenue_chart = create_revenue_chart(
        customer_df
    )

    table_data = (
        customer_df
        .head(15)
        .to_dict("records")
    )

    return render_template(

        "dashboard.html",

        customers=
        metrics["Total Customers"],

        revenue=
        metrics["Total Revenue"],

        avg_age=
        metrics["Average Age"],

        revenue_chart=
        revenue_chart,

        insights=
        insights,

        table_data=
        table_data
    )

# ============================
# Segmentation
# ============================

@app.route('/segmentation')
def segmentation():

    global customer_df

    if customer_df is None:

        return redirect(
            url_for('home')
        )

    segmented_df = perform_segmentation(
        customer_df.copy()
    )

    chart_path = create_segment_chart(
        segmented_df
    )

    segment_counts = (
        segmented_df["Segment"]
        .value_counts()
        .to_dict()
    )

    table_data = (
        segmented_df
        .head(100)
        .to_dict("records")
    )

    return render_template(

        "segmentation.html",

        segment_counts=
        segment_counts,

        chart_path=
        chart_path,

        table_data=
        table_data
    )

# ============================
# Prediction
# ============================

@app.route('/prediction')
def prediction():

    global customer_df

    if customer_df is None:

        return redirect(
            url_for('home')
        )

    predictions = (
        predict_churn_customers(
            customer_df
        )
    )

    high_risk = len([

        p for p in predictions

        if p["Probability"] > 80

    ])

    active_customers = len([

        p for p in predictions

        if p["Prediction"] == "Active"

    ])

    return render_template(

        "prediction.html",

        predictions=
        predictions,

        high_risk=
        high_risk,

        active_customers=
        active_customers
    )

# ============================
# Recommendation
# ============================

@app.route('/recommendation')
def recommendation():

    global customer_df

    if customer_df is None:

        return redirect(
            url_for('home')
        )

    recommendations = []

    for _, row in customer_df.head(20).iterrows():

        recommendations.append({

            "CustomerID":
            row["CustomerID"],

            "Products":
            recommend_products(
                row["SpendingScore"]
            )
        })

    return render_template(

        "recommendation.html",

        recommendations=
        recommendations
    )

# ============================
# Customer Search
# ============================

@app.route(
    '/customer_search',
    methods=['GET']
)
def customer_search():

    global customer_df

    customer = None

    customer_id = request.args.get(
        'customer_id'
    )

    if customer_id and customer_df is not None:

        result = customer_df[
            customer_df["CustomerID"]
            .astype(str)
            ==
            customer_id
        ]

        if not result.empty:

            customer = (
                result.iloc[0]
                .to_dict()
            )

    return render_template(

        "customer_search.html",

        customer=
        customer
    )

# ============================
# Download CSV
# ============================

@app.route('/download')
def download():

    global customer_df

    if customer_df is None:

        return "No Dataset Available"

    output_file = os.path.join(

        app.config['UPLOAD_FOLDER'],

        "processed_data.csv"
    )

    customer_df.to_csv(
        output_file,
        index=False
    )

    return redirect(

        url_for(
            'static',
            filename=
            'uploads/processed_data.csv'
        )
    )

# ============================
# Export Excel
# ============================

@app.route('/export_excel')
def export_excel():

    global customer_df

    if customer_df is None:

        return "No Dataset Available"

    file_path = os.path.join(

        app.config['UPLOAD_FOLDER'],

        "customer_report.xlsx"
    )

    customer_df.to_excel(
        file_path,
        index=False
    )

    return redirect(

        url_for(
            'static',
            filename=
            'uploads/customer_report.xlsx'
        )
    )

# ============================
# Single Customer Analysis
# ============================

@app.route('/customer/<int:customer_id>')
def customer_analysis(customer_id):

    global customer_df

    if customer_df is None:

        return redirect(
            url_for('home')
        )

    customer = customer_df[
        customer_df["CustomerID"]
        ==
        customer_id
    ]

    if customer.empty:

        return "Customer Not Found"

    customer = customer.iloc[0]

    prediction = predict_purchase_value(
        customer["SpendingScore"]
    )

    products = recommend_products(
        customer["SpendingScore"]
    )

    return {

        "CustomerID":
        int(customer["CustomerID"]),

        "Predicted Revenue":
        prediction,

        "Recommendations":
        products
    }

# ============================
# 404 Page
# ============================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404

# ============================
# Run App
# ============================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )