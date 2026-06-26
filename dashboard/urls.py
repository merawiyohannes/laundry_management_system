from django.urls import path
from .views import dashboard, worker_dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("worker/", worker_dashboard, name="worker_dashboard"),

]