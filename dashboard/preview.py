from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset
import pandas as pd
import math

@login_required
def data_preview(request):

    # Get latest uploaded dataset
    dataset = Dataset.objects.filter(
        user=request.user
    ).order_by("-uploaded_at").first()

    if not dataset:
        return render(request, "preview.html", {
            "error": "No dataset uploaded."
        })

    # Read uploaded file
    if dataset.file.name.endswith(".csv"):
        df = pd.read_csv(dataset.file.path)
    else:
        df = pd.read_excel(dataset.file.path)

    # Get search text
    search = request.GET.get("search", "")

    # Filter rows if search text is entered
    if search:
        df = df[
            df.astype(str)
            .apply(lambda row: row.str.contains(search, case=False).any(), axis=1)
        ]

    # Total rows after search
    total_rows = len(df)

    # Current page
    page = int(request.GET.get("page", 1))

    # Rows per page
    rows_per_page = 20

    # Calculate start and end
    start = (page - 1) * rows_per_page
    end = start + rows_per_page

    # Show only current page
    df = df.iloc[start:end]
    total_pages = math.ceil(total_rows / rows_per_page)

    # Convert dataframe to HTML
    preview = df.to_html(
        classes="table table-bordered table-striped",
        index=False
    )

    context = {
        "preview": preview,
        "dataset_name": dataset.name,
        "uploaded_at": dataset.uploaded_at,
        "total_rows": total_rows,
        "total_columns": len(df.columns),

        "page": page,
        "total_pages": total_pages,
        "search": search,
    }
    return render(request, "preview.html", context)