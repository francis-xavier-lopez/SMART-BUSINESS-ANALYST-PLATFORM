import pandas as pd


def prepare_monthly_data(df, mapping):
    """
    Convert the date column to datetime and
    calculate monthly revenue.
    """

    df[mapping.date_column] = pd.to_datetime(df[mapping.date_column])

    monthly_data = (
        df.groupby(
            df[mapping.date_column].dt.to_period("M")
        )[mapping.revenue_column]
        .sum()
        .reset_index()
    )

    # Rename columns to fixed names
    monthly_data.columns = ["month", "revenue"]

    # Convert month to string
    monthly_data["month"] = monthly_data["month"].astype(str)

    return monthly_data


def forecast_next_month(monthly_data, mapping):
    """
    Simple forecast:
    Predict next month's revenue
    using the average monthly growth.
    """

    revenues = monthly_data["revenue"].tolist()

    if len(revenues) < 2:
        return revenues[-1]

    growth = []

    for i in range(1, len(revenues)):
        growth.append(revenues[i] - revenues[i - 1])

    average_growth = sum(growth) / len(growth)

    prediction = revenues[-1] + average_growth

    return round(prediction, 2)