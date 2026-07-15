from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset, ColumnMapping
from .services import calculate_kpis
from .charts import generate_charts
from .utils import detect_columns
from .preview import data_preview
from .upload import upload_file
from .insights import ai_insights
from .forecast import forecast
from .reports import reports, download_report
from .datasets import dataset_list, use_dataset
import math
import pandas as pd

# Create your views here.

@login_required
def dashboard(request):

    # Get latest uploaded dataset
    dataset = Dataset.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    if not dataset:
        return render(request, "dashboard.html", {
            "error": "No dataset uploaded."
        })

    # Get saved column mapping
    mapping = ColumnMapping.objects.get(dataset=dataset)

    # Read uploaded file
    if dataset.file.name.endswith(".csv"):
        df = pd.read_csv(dataset.file.path)
    else:
        df = pd.read_excel(dataset.file.path)

    # Calculate KPI values
    kpis = calculate_kpis(df, mapping)

    # Generate all chart data
    charts = generate_charts(df, mapping)


    context = {
        **kpis,
        **charts,
    }

    return render(request, "dashboard.html", context)
