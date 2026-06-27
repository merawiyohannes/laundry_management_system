from django.urls import path
from . import views

urlpatterns = [
    # path("create/", views.create_payment, name="create_payment"),
    path("", views.payment_list, name="payment_list"),
    path("order/<int:order_id>/create/", views.create_payment, name="create_payment"),
]