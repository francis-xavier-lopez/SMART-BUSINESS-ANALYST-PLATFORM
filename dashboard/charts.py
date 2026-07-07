import pandas as pd


def generate_charts(df, mapping):
    """
    Generate all chart data for the dashboard.
    """

    # Convert date column to datetime
    df[mapping.date_column] = pd.to_datetime(df[mapping.date_column])

    # -------------------------
    # Revenue Trend Chart
    # -------------------------
    revenue_data = (
        df.groupby(mapping.date_column)[mapping.revenue_column]
        .sum()
        .reset_index()
    )

    chart_labels = revenue_data[mapping.date_column].dt.strftime("%d-%m-%Y").tolist()
    chart_values = revenue_data[mapping.revenue_column].tolist()

    # -------------------------
    # Monthly Revenue Chart
    # -------------------------
    df["Month"] = df[mapping.date_column].dt.strftime("%b")

    monthly_data = (
        df.groupby("Month")[mapping.revenue_column]
        .sum()
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_data = monthly_data.reindex(month_order).dropna()

    monthly_labels = monthly_data.index.tolist()
    monthly_values = monthly_data.values.tolist()

    # -------------------------
    # Product Performance Chart
    # -------------------------
    product_data = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    product_labels = product_data.index.tolist()
    product_values = product_data.values.tolist()

    # -------------------------
    # Category Revenue Chart
    # -------------------------
    category_data = (
        df.groupby(mapping.category_column)[mapping.revenue_column]
        .sum()
        .sort_values(ascending=False)
    )

    category_labels = category_data.index.tolist()
    category_values = category_data.values.tolist()

    return {
        "chart_labels": chart_labels,
        "chart_values": chart_values,

        "product_labels": product_labels,
        "product_values": product_values,

        "category_labels": category_labels,
        "category_values": category_values,

        "monthly_labels": monthly_labels,
        "monthly_values": monthly_values,
    }