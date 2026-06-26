from django.shortcuts import render
import pandas as pd

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("datafile")

        if uploaded_file:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)

            else:
                return render(request, "upload.html", {
                    "error": "Only CSV and Excel files are allowed."
                })

            print(df.head())   # Check in the terminal

            return render(request, "upload.html", {
                "success": "File uploaded successfully!"
            })

    return render(request, "upload.html")