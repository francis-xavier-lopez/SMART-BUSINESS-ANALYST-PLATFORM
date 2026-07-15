from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset, ColumnMapping
from .utils import detect_columns
import pandas as pd

@login_required
def upload_file(request):

    if request.method == "POST":

        uploaded_file = request.FILES.get("datafile")

        if not uploaded_file:
            return render(request, "upload.html", {
                "error": "Please choose a file."
            })

        # Check file type
        if not (
            uploaded_file.name.endswith(".csv")
            or uploaded_file.name.endswith(".xlsx")
        ):
            return render(request, "upload.html", {
                "error": "Only CSV and Excel files are allowed."
            })

        # Make all previous datasets inactive
        Dataset.objects.filter(
            user=request.user
        ).update(is_active=False)

        # Save dataset
        dataset = Dataset.objects.create(
            user=request.user,
            name=uploaded_file.name,
            file=uploaded_file,
            is_active=True
        )

        # Read file
        if dataset.file.name.endswith(".csv"):
            df = pd.read_csv(dataset.file.path)
        else:
            df = pd.read_excel(dataset.file.path)

        # Get column names
        columns = df.columns.tolist()

        # Generate preview
        preview = df.head().to_html(
            classes="table table-bordered table-striped table-hover",
            index=False
        )

        # Auto detect important columns
        detected_columns = detect_columns(df)

        print(detected_columns)

        # Required columns
        required_fields = [
            "revenue",
            "sales",
            "product",
            "date"
        ]

        # Check only required columns
        if not all(detected_columns[field] for field in required_fields):
            return render(request, "upload.html", {
                "error": "Some columns could not be detected automatically. Please map them manually.",
                "preview": preview,
                "columns": columns,
            })

        # Save column mapping
        ColumnMapping.objects.create(
            dataset=dataset,
            revenue_column=detected_columns["revenue"],
            sales_column=detected_columns["sales"],
            product_column=detected_columns["product"],
            date_column=detected_columns["date"],
            category_column=detected_columns.get("category") or ""
        )

        return render(request, "upload.html", {
            "success": "File uploaded successfully!",
            "preview": preview,
            "columns": columns,
        })
    return render(request, "upload.html")
