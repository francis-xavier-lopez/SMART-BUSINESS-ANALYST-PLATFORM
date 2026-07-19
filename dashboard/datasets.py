from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Business_app.models import Dataset
import os


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

@login_required
def delete_dataset(request, dataset_id):

    dataset = Dataset.objects.filter(
        id=dataset_id,
        user=request.user
    ).first()

    if dataset:

        # Delete uploaded file
        if dataset.file and os.path.isfile(dataset.file.path):
            os.remove(dataset.file.path)

        # Remember if this dataset was active
        was_active = dataset.is_active

        # Delete database record
        dataset.delete()

        # If the deleted dataset was active,
        # activate the latest remaining dataset
        if was_active:

            # First make sure all remaining datasets are inactive
            Dataset.objects.filter(
                user=request.user
            ).update(is_active=False)

            latest = Dataset.objects.filter(
                user=request.user
            ).order_by("-uploaded_at").first()

            if latest:

                latest.is_active = True
                latest.save()

    return redirect("/dashboard/datasets/?deleted=1")