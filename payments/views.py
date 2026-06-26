from django.shortcuts import render, redirect
from orders.models import Order
from .models import Payment

def create_payment(request):
    orders = Order.objects.all()

    if request.method == "POST":
        order_id = request.POST.get("order")
        amount = float(request.POST.get("amount"))
        method = request.POST.get("method")

        order = Order.objects.get(id=order_id)

        Payment.objects.create(
            order=order,
            amount=amount,
            payment_method=method
        )

        return redirect(f"/orders/{order.id}/")

    return render(request, "payments/create_payment.html", {
        "orders": orders
    })    
    

def payment_list(request):

    payments = Payment.objects.select_related(
        "order",
        "order__customer"
    ).order_by("-created_at")

    return render(
        request,
        "payments/payment_list.html",
        {
            "payments": payments
        }
    )