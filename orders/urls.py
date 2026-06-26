from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("create/", views.order_create, name="order_create"),
    path("<int:order_id>/", views.order_detail, name="order_detail"),
    path("<int:order_id>/status/<str:action>/", views.update_status, name="update_status"),
    path("<int:order_id>/pay-remaining/", views.pay_remaining, name="pay_remaining"),
]