from django.urls import path
from .views import login_view, logout_view, create_worker
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create-worker/", create_worker, name="create_worker"),
    path("password-change/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change.html"
    ), name="password_change"),

    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_done.html"
    ), name="password_change_done"),
]