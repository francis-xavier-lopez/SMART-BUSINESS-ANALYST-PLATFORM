from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset, ColumnMapping
import pandas as pd
from .ai import generate_ai_insights

@login_required
def ai_insights(request):

    # Get latest uploaded dataset
    dataset = Dataset.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    if not dataset:
        return render(request, "ai.html", {
            "error": "No dataset uploaded."
        })

    # Get saved column mapping
    mapping = ColumnMapping.objects.get(dataset=dataset)

    # Read uploaded file
    if dataset.file.name.endswith(".csv"):
        df = pd.read_csv(dataset.file.path)
    else:
        df = pd.read_excel(dataset.file.path)

    # Generate AI Insights
    insights = generate_ai_insights(df, mapping)

    context = {
        "dataset_name": dataset.name,
        "insights": insights,
    }

    return render(request, "ai.html", context)