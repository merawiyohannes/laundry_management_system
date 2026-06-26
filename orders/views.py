from django.shortcuts import render, redirect

from customers.models import Customer
from services.models import Service
from .models import Order, OrderLine

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from payments.models import Payment


def pay_remaining(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    remaining = order.balance_due

    if remaining > 0:
        Payment.objects.create(
            order=order,
            amount=remaining,
            payment_method="CASH"
        )

    return redirect(f"/orders/{order.id}/")

def order_list(request):
    orders = Order.objects.all().order_by("-id")

    return render(request, "orders/order_list.html", {
        "orders": orders
    })
    
def order_create(request):

    customers = Customer.objects.all()
    services = Service.objects.filter(is_active=True)

    if request.method == "POST":

        customer_id = request.POST.get("customer")
        customer = Customer.objects.get(id=customer_id)

        order = Order.objects.create(customer=customer)

        # 🔥 INFINITE ITEMS HANDLING
        service_ids = request.POST.getlist("service")
        quantities = request.POST.getlist("quantity")

        for service_id, qty in zip(service_ids, quantities):

            if service_id and qty:
                OrderLine.objects.create(
                    order=order,
                    service_id=service_id,
                    quantity=qty
                )

        return redirect("order_list")

    return render(request, "orders/order_create.html", {
        "customers": customers,
        "services": services
    })
            
def order_detail(request, order_id):

    order = Order.objects.get(id=order_id)

    return render(request, "orders/order_detail.html", {
        "order": order
    })
    
def update_status(request, order_id, action):

    order = get_object_or_404(Order, id=order_id)

    # BUSINESS RULE: cannot collect if not paid
    if action == "COLLECTED" and not order.is_fully_paid:
        return HttpResponse("Cannot collect. Payment not completed.")

    valid_transitions = [
        "RECEIVED",
        "WASHING",
        "DRYING",
        "IRONING",
        "READY",
        "COLLECTED",
    ]

    if action in valid_transitions:
        order.status = action
        order.save()

    return redirect("order_detail", order_id=order.id)