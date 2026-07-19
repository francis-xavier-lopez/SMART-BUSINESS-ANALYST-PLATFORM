import pandas as pd


def generate_charts(df, mapping):
    """
    Generate all chart data for the dashboard.
    """

    # Convert date column to datetime
    df[mapping.date_column] = pd.to_datetime(df[mapping.date_column])

    # -------------------------
    # Revenue Trend Chart (Dynamic)
    # -------------------------

    # Sort data by date
    df = df.sort_values(mapping.date_column)

    total_rows = len(df)

    # ---------- Daily ----------
    if total_rows <= 30:

        revenue_data = (
            df.groupby(mapping.date_column)[mapping.revenue_column]
            .sum()
            .reset_index()
        )

        chart_labels = (
            revenue_data[mapping.date_column]
            .dt.strftime("%d-%m-%Y")
            .tolist()
        )

        chart_values = revenue_data[mapping.revenue_column].tolist()

        revenue_chart_title = "Daily Revenue"

    # ---------- 5-Day ----------
    elif total_rows <= 150:

        df = df.reset_index(drop=True)

        df["Group"] = df.index // 5

        revenue_data = (
            df.groupby("Group")
            .agg({
                mapping.revenue_column: "sum",
                mapping.date_column: ["min", "max"]
            })
        )

        revenue_data.columns = ["Revenue", "Start", "End"]

        chart_labels = (
                revenue_data["Start"].dt.strftime("%d %b")
                + " - " +
                revenue_data["End"].dt.strftime("%d %b")
        ).tolist()

        chart_values = revenue_data["Revenue"].tolist()

        revenue_chart_title = "5-Day Revenue"

    # ---------- Monthly ----------
    elif total_rows <= 365:

        df["Month"] = df[mapping.date_column].dt.strftime("%b %Y")

        revenue_data = (
            df.groupby("Month")[mapping.revenue_column]
            .sum()
            .reset_index()
        )

        chart_labels = revenue_data["Month"].tolist()

        chart_values = revenue_data[mapping.revenue_column].tolist()

        revenue_chart_title = "Monthly Revenue"

    # ---------- Quarterly ----------
    else:

        df["Quarter"] = df[mapping.date_column].dt.to_period("Q").astype(str)

        revenue_data = (
            df.groupby("Quarter")[mapping.revenue_column]
            .sum()
            .reset_index()
        )

        chart_labels = revenue_data["Quarter"].tolist()

        chart_values = revenue_data[mapping.revenue_column].tolist()

        revenue_chart_title = "Quarterly Revenue"

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
        "revenue_chart_title": revenue_chart_title,
        "chart_labels": chart_labels,
        "chart_values": chart_values,

        "product_chart_title": "Top 10 Products by Revenue",
        "product_labels": product_labels,
        "product_values": product_values,

        "category_chart_title": "Revenue by Category",
        "category_labels": category_labels,
        "category_values": category_values,

        "monthly_chart_title": "Monthly Revenue",
        "monthly_labels": monthly_labels,
        "monthly_values": monthly_values,
    }