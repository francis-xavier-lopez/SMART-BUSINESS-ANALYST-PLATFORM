def calculate_kpis(df, mapping):

    total_revenue = df[mapping.revenue_column].sum()
    total_sales = df[mapping.sales_column].sum()
    total_products = df[mapping.product_column].nunique()
    average_revenue = round(df[mapping.revenue_column].mean(), 2)

    return {
        "total_revenue": f"{total_revenue:,.0f}",
        "total_sales": f"{total_sales:,}",
        "total_products": f"{total_products:,}",
        "average_revenue": f"{average_revenue:,.2f}",
    }