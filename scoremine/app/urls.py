from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_, name="login"),
    path("register_request", views.register_request, name="register"),
    path("login_request", views.login_request, name="login"),
    path('activate/<username>/<email>/<pass1>', views.activate, name='activate'),
    path("logout_request", views.logout_request, name="logout")
]