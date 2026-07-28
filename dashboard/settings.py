from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from Business_app.models import Dataset
import os

@login_required
def settings_view(request):

    if request.method == "POST":

        user = request.user

        user.username = request.POST.get("username")
        user.email = request.POST.get("email")

        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Change password only if user entered values
        if current_password or new_password or confirm_password:

            if not user.check_password(current_password):

                messages.error(request, "Current password is incorrect.")

                return redirect("settings")

            if new_password != confirm_password:

                messages.error(request, "New passwords do not match.")

                return redirect("settings")

            user.set_password(new_password)

            user.save()

            # Force user to login again
            logout(request)

            messages.success(
                request,
                "Password updated successfully. Please login again."
            )

            return redirect("login")

        user.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("settings")

    return render(request, "settings.html")



@login_required
def delete_account(request):

    if request.method == "POST":

        password = request.POST.get("delete_password")

        user = request.user

        # Verify password
        if not user.check_password(password):

            messages.error(request, "Incorrect password.")

            return redirect("settings")

        # Delete all uploaded dataset files
        datasets = Dataset.objects.filter(user=user)

        for dataset in datasets:

            if dataset.file and os.path.isfile(dataset.file.path):

                os.remove(dataset.file.path)

        # Delete dataset records
        datasets.delete()

        # Logout user
        logout(request)

        # Delete account
        user.delete()

        messages.success(
            request,
            "Your account has been deleted successfully."
        )

        return redirect("login")

    return redirect("settings")