from django.urls import path
from invest.views import HomeView, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("users/register/", UserRegisterView.as_view(), name="user_register"),
    path("users/login/", UserLoginView.as_view(), name="login"),
    path("users/logout/", UserLogoutView.as_view(), name="logout")
]
