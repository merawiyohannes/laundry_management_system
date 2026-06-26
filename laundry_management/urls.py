
from django.contrib import admin
from django.urls import path, include
from .views import home, track_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path("customers/", include("customers.urls")),
    path("services/", include("services.urls")),
    path("orders/", include("orders.urls")),
    path("payments/", include("payments.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("", home, name="home"),
    path("track/", track_order, name="track_order"),
    
]
