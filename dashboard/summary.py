def generate_business_summary(df, mapping):

    total_revenue = df[mapping.revenue_column].sum()

    total_sales = df[mapping.sales_column].sum()

    total_products = df[mapping.product_column].nunique()

    average_revenue = round(
        df[mapping.revenue_column].mean(),
        2
    )

    top_product = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
        .idxmax()
    )

    top_product_revenue = (
        df.groupby(mapping.product_column)[mapping.revenue_column]
        .sum()
        .max()
    )

    if mapping.category_column:

        top_category = (
            df.groupby(mapping.category_column)[mapping.revenue_column]
            .sum()
            .idxmax()
        )

    else:

        top_category = "Not Available"

    summary = f"""
Business Summary

Dataset contains {len(df)} records.

Total Revenue : ₹{total_revenue:,.0f}

Total Sales : {total_sales:,}

Total Products : {total_products}

Average Revenue : ₹{average_revenue:,.2f}

Top Product : {top_product}

Top Product Revenue : ₹{top_product_revenue:,.0f}

Best Category : {top_category}
"""

    return summary