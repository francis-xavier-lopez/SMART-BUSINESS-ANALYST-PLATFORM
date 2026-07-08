import pandas as pd

def highest_revenue_product(df, mapping):

    product_revenue = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
    )

    top_product = product_revenue.idxmax()
    top_revenue = product_revenue.max()

    return {
        "icon": "🏆",
        "title": "Highest Revenue Product",
        "value": top_product,
        "description": f"Generated ₹{top_revenue:,.0f} revenue"
    }

def lowest_revenue_product(df, mapping):

    product_revenue = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
    )

    lowest_product = product_revenue.idxmin()
    lowest_revenue = product_revenue.min()

    return {
        "icon": "📉",
        "title": "Lowest Revenue Product",
        "value": lowest_product,
        "description": f"Generated only ₹{lowest_revenue:,.0f} revenue"
    }

def best_category(df, mapping):

    # Check if category column exists
    if not mapping.category_column:
        return {
            "icon": "📦",
            "title": "Best Category",
            "value": "Not Available",
            "description": "No category column was mapped."
        }

    category_revenue = (
        df.groupby(mapping.category_column)[mapping.revenue_column]
        .sum()
    )

    top_category = category_revenue.idxmax()
    top_revenue = category_revenue.max()

    return {
        "icon": "📦",
        "title": "Best Revenue Category",
        "value": top_category,
        "description": f"Generated ₹{top_revenue:,.0f} revenue"
    }

def best_month(df, mapping):

    # Convert date column to datetime
    df[mapping.date_column] = pd.to_datetime(df[mapping.date_column])

    # Create Month column
    df["Month"] = df[mapping.date_column].dt.strftime("%B")

    month_revenue = (
        df.groupby("Month")[mapping.revenue_column]
        .sum()
    )

    top_month = month_revenue.idxmax()
    top_revenue = month_revenue.max()

    return {
        "icon": "📅",
        "title": "Best Revenue Month",
        "value": top_month,
        "description": f"Generated ₹{top_revenue:,.0f} revenue"
    }

def business_recommendation(df, mapping):

    product_revenue = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
    )

    top_product = product_revenue.idxmax()
    top_revenue = product_revenue.max()

    total_revenue = product_revenue.sum()

    contribution = (top_revenue / total_revenue) * 100

    recommendation = (
        f"{top_product} contributes "
        f"{contribution:.1f}% of total revenue. "
        "Consider increasing inventory, running targeted promotions, "
        "and bundling this product with related items."
    )

    return {
        "icon": "💡",
        "title": "AI Recommendation",
        "value": top_product,
        "description": recommendation
    }


def generate_ai_insights(df, mapping):

    insights = []

    insights.append(
        highest_revenue_product(df, mapping)
    )

    insights.append(
        lowest_revenue_product(df, mapping)
    )

    insights.append(
        best_category(df, mapping)
    )

    insights.append(
        best_month(df, mapping)
    )

    insights.append(
        business_recommendation(df, mapping)
    )

    return insights