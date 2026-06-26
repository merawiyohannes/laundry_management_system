from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all().order_by("-id")
    return render(request, "customers/customer_list.html", {
        "customers": customers
    })
def customer_create(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        Customer.objects.create(
            name=name,
            phone=phone,
            address=address
        )

        return redirect("customer_list")

    return render(request, "customers/customer_create.html")