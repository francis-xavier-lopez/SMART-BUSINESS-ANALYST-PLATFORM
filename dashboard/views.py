from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset
from .utils import detect_columns
import pandas as pd

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("datafile")

        if uploaded_file:

            # Save file in the database
            dataset = Dataset.objects.create(
                user=request.user,
                name=uploaded_file.name,
                file=uploaded_file
            )

            # Read the saved file
            if dataset.file.name.endswith(".csv"):
                df = pd.read_csv(dataset.file.path)
                columns = df.columns.tolist()

            elif dataset.file.name.endswith(".xlsx"):
                df = pd.read_excel(dataset.file.path)
                columns = df.columns.tolist()

            else:
                return render(request, "upload.html", {
                    "error": "Only CSV and Excel files are allowed."
                })

            # Detect columns
            detected_columns = detect_columns(df)
            print(detected_columns)

            # Generate preview
            preview = df.head().to_html(
                classes="table table-bordered",
                index=False
            )

            return render(request, "upload.html", {
                "success": "File uploaded successfully!",
                "preview": preview,
                "columns": columns
            })

    return render(request, "upload.html")