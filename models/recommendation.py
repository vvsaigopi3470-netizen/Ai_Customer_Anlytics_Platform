# models/recommendation.py

def recommend_products(spending_score):

    spending_score = float(spending_score)

    if spending_score >= 80:

        return [

            "Premium Membership",

            "Luxury Products",

            "Exclusive Offers",

            "VIP Rewards"
        ]

    elif spending_score >= 60:

        return [

            "Electronics",

            "Fashion Items",

            "Special Discounts"
        ]

    elif spending_score >= 40:

        return [

            "Home Essentials",

            "Kitchen Products",

            "Seasonal Offers"
        ]

    else:

        return [

            "Budget Deals",

            "Discount Coupons",

            "Starter Packages"
        ]


def generate_customer_recommendations(df):

    recommendations = []

    for _, row in df.iterrows():

        recommendations.append({

            "CustomerID":
            int(row["CustomerID"]),

            "Products":
            recommend_products(
                row["SpendingScore"]
            )
        })

    return recommendations