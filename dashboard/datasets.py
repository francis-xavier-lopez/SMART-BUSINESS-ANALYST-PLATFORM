from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Business_app.models import Dataset


@login_required
def dataset_list(request):

    datasets = Dataset.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    active_dataset = Dataset.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    return render(
        request,
        "datasets.html",
        {
            "datasets": datasets,
            "active_dataset": active_dataset,
        }
    )

@login_required
def use_dataset(request, dataset_id):

    Dataset.objects.filter(
        user=request.user
    ).update(is_active=False)

    Dataset.objects.filter(
        id=dataset_id,
        user=request.user
    ).update(is_active=True)

    return redirect("/dashboard/datasets/?success=1")