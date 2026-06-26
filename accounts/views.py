from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required


def login_view(request):

    if request.user.is_authenticated:
        return redirect("/dashboard/")

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # ROLE ROUTING
            if user.is_superuser:
                return redirect("/dashboard/")
            else:
                return redirect("/dashboard/worker/")

        return render(request, "accounts/login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")


@staff_member_required
def create_worker(request):

    if request.method == "POST":

        name = request.POST["name"]
        phone = request.POST["phone"]
        password = request.POST["password"]

        username = phone  # simple unique login

        User.objects.create_user(
            username=username,
            password=password,
            first_name=name
        )

        return redirect("/dashboard/")

    return render(request, "accounts/create_worker.html")