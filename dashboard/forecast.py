from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Business_app.models import Dataset, ColumnMapping

import pandas as pd

from .forecasting import (
    prepare_monthly_data,
    forecast_next_month
)


@login_required
def forecast(request):

    # Get latest uploaded dataset
    dataset = Dataset.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    if not dataset:
        return render(request, "forecast.html", {
            "error": "No dataset uploaded."
        })

    # Get saved column mapping
    mapping = ColumnMapping.objects.get(
        dataset=dataset
    )

    # Read uploaded file
    if dataset.file.name.endswith(".csv"):
        df = pd.read_csv(dataset.file.path)
    else:
        df = pd.read_excel(dataset.file.path)

    # Prepare monthly revenue
    monthly_data = prepare_monthly_data(df, mapping)

    # Predict next month
    prediction = forecast_next_month(
        monthly_data,
        mapping
    )

    print(monthly_data)

    context = {
        "dataset_name": dataset.name,

        "monthly_data": monthly_data.to_dict("records"),

        "prediction": prediction,

        "months": monthly_data["month"].tolist(),

        "revenues": monthly_data["revenue"].tolist(),
    }

    return render(
        request,
        "forecast.html",
        context
    )