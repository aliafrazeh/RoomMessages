from django.urls import path
from django.contrib.auth import views
from .views import RegisterView
app_name = "account"

urlpatterns = [
    path("",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path('register/',RegisterView.as_view(),name="register"),
]