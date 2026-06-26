from django.urls import path
from . import views

urlpatterns = [
    path("", views.service_list, name="service_list"),
    path("create/", views.service_create, name="service_create"),
]