from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from orders.models import Order
from payments.models import Payment
from django.utils import timezone
from datetime import timedelta

from customers.models import Customer
from django.contrib.auth.models import User


@login_required
def dashboard(request):

    today = timezone.now().date()
    week_start = today - timedelta(days=7)

    # Orders
    orders_today = Order.objects.filter(created_at__date=today).count()
    active_orders = Order.objects.exclude(status="COLLECTED").count()
    ready_orders = Order.objects.filter(status="READY").count()

    # Revenue
    revenue_today = sum(
        p.amount for p in Payment.objects.filter(created_at__date=today)
    )

    revenue_week = sum(
        p.amount for p in Payment.objects.filter(created_at__date__gte=week_start)
    )

    total_revenue = sum(
        p.amount for p in Payment.objects.all()
    )

    # Business size
    total_customers = Customer.objects.count()
    total_payments = Payment.objects.count()
    total_orders = Order.objects.count()

    # Workers (non-superusers)
    total_workers = User.objects.filter(is_superuser=False).count()

    context = {
        "orders_today": orders_today,
        "active_orders": active_orders,
        "ready_orders": ready_orders,

        "revenue_today": revenue_today,
        "revenue_week": revenue_week,
        "total_revenue": total_revenue,

        "total_customers": total_customers,
        "total_payments": total_payments,
        "total_orders": total_orders,
        "total_workers": total_workers,
    }

    return render(request, "dashboard/dashboard.html", context)

@login_required
def worker_dashboard(request):
    return render(request, "dashboard/worker_dashboard.html")