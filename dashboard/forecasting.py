from sklearn.linear_model import LinearRegression
import numpy as np
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

    revenues = monthly_data["revenue"].values

    # X = Month numbers
    X = np.arange(len(revenues)).reshape(-1, 1)

    # Y = Revenue
    y = revenues

    model = LinearRegression()

    model.fit(X, y)

    # Predict next month
    next_month = np.array([[len(revenues)]])

    prediction = model.predict(next_month)

    return round(float(prediction[0]), 2)