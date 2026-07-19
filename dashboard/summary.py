import pandas as pd


def generate_business_summary(df, mapping):

    total_revenue = df[mapping.revenue_column].sum()
    total_sales = df[mapping.sales_column].sum()
    total_products = df[mapping.product_column].nunique()
    average_revenue = df[mapping.revenue_column].mean()

    # ---------- Top 5 Products ----------

    top_products = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    top_products_text = ""

    for product, revenue in top_products.items():

        top_products_text += f"{product} : ₹{revenue:,.0f}\n"

    # ---------- Category Revenue ----------

    if mapping.category_column:

        category_revenue = (
            df.groupby(mapping.category_column)[mapping.revenue_column]
            .sum()
            .sort_values(ascending=False)
        )

        category_text = ""

        for category, revenue in category_revenue.items():

            category_text += f"{category} : ₹{revenue:,.0f}\n"

    else:

        category_text = "No category available."

    # ---------- Monthly Revenue ----------

    df[mapping.date_column] = pd.to_datetime(
        df[mapping.date_column],
        format="%d-%m-%Y"
    )

    df["Month"] = df[mapping.date_column].dt.strftime("%B")

    monthly_revenue = (
        df.groupby("Month")[mapping.revenue_column]
        .sum()
    )

    monthly_text = ""

    for month, revenue in monthly_revenue.items():

        monthly_text += f"{month} : ₹{revenue:,.0f}\n"

    summary = f"""
Business Summary

Total Revenue : ₹{total_revenue:,.0f}

Total Sales : {total_sales}

Total Products : {total_products}

Average Revenue : ₹{average_revenue:,.0f}

Top Products

{top_products_text}

Category Revenue

{category_text}

Monthly Revenue

{monthly_text}
"""

    return summary