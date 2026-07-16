import pandas as pd

def calculate_kpis(df, mapping):

    total_revenue = df[mapping.revenue_column].sum()
    total_sales = df[mapping.sales_column].sum()
    total_products = df[mapping.product_column].nunique()
    average_revenue = round(df[mapping.revenue_column].mean(), 2)

    # ---------- Growth Calculation ----------

    growth = 0

    try:

        df[mapping.date_column] = pd.to_datetime(df[mapping.date_column])

        monthly = (
            df.groupby(
                df[mapping.date_column].dt.to_period("M")
            )[mapping.revenue_column]
            .sum()
            .sort_index()
        )

        if len(monthly) >= 2:

            previous = monthly.iloc[-2]
            current = monthly.iloc[-1]

            if previous != 0:
                growth = round(
                    ((current - previous) / previous) * 100,
                    2
                )

    except Exception:
        growth = 0

    return {

        "total_revenue": f"{total_revenue:,.0f}",

        "total_sales": f"{total_sales:,}",

        "total_products": f"{total_products:,}",

        "average_revenue": f"{average_revenue:,.2f}",

        "growth": growth,

    }