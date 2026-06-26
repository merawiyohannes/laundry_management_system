from django.shortcuts import render
from orders.models import Order


def home(request):
    return render(request, "home.html")


def track_order(request):

    query = request.GET.get("q")

    order = None

    if query:

        # Search by receipt number
        order = Order.objects.filter(
            receipt_number__iexact=query
        ).first()

        # If not found, search by phone
        if not order:

            order = Order.objects.filter(
                customer__phone__icontains=query
            ).order_by("-id").first()

    return render(request, "track_order.html", {
        "order": order,
        "query": query
    })