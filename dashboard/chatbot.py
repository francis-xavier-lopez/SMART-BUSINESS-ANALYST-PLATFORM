from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Business_app.models import Dataset, ColumnMapping
from .gemini_service import ask_gemini
from .summary import generate_business_summary
import pandas as pd


@login_required
def chatbot(request):

    answer = ""

    if request.method == "POST":

        question = request.POST.get("question", "")

        dataset = Dataset.objects.filter(
            user=request.user,
            is_active=True
        ).first()

        if dataset:

            mapping = ColumnMapping.objects.get(dataset=dataset)

            if dataset.file.name.endswith(".csv"):
                df = pd.read_csv(dataset.file.path)
            else:
                df = pd.read_excel(dataset.file.path)

            summary = generate_business_summary(df, mapping)

            prompt = f"""
        You are an expert Business Data Analyst.

        Business Summary:

        {summary}

        User Question:

        {question}

        Rules:

        1. Answer only using the business summary.
        2. If the information is unavailable, clearly say so.
        3. Keep the answer professional.
        4. Give business recommendations whenever appropriate.

        Answer:
        """

            answer = ask_gemini(prompt)

    return render(
        request,
        "chatbot.html",
        {
            "answer": answer
        }
    )

