from django.shortcuts import render, redirect
from .models import Service
from django.contrib.auth.decorators import login_required, user_passes_test


def is_owner(user):
    return user.is_superuser

@user_passes_test(is_owner)
def service_list(request):
    services = Service.objects.all().order_by("-id")

    return render(request, "services/service_list.html", {
        "services": services
    })
 
 
@user_passes_test(is_owner) 
def service_create(request):

    if request.method == "POST":
        name = request.POST.get("name")
        pricing_type = request.POST.get("pricing_type")
        unit_price = request.POST.get("unit_price")

        Service.objects.create(
            name=name,
            pricing_type=pricing_type,
            unit_price=unit_price
        )

        return redirect("service_list")

    return render(request, "services/service_create.html")