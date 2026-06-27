from django.shortcuts import render, redirect
from orders.models import Order
from .models import Payment

def create_payment(request, order_id):
    order = Order.objects.get(id=order_id)

    # BLOCK fully paid orders
    if order.balance_due <= 0:
        return redirect(f"/orders/{order.id}/")

    if request.method == "POST":

        amount = float(request.POST.get("amount"))
        method = request.POST.get("method")

        # BLOCK overpayment
        if amount > order.balance_due:
            amount = order.balance_due  # or reject instead

        Payment.objects.create(
            order=order,
            amount=amount,
            payment_method=method
        )

        return redirect(f"/orders/{order.id}/")

    return render(request, "payments/create_payment.html", {
        "order": order
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