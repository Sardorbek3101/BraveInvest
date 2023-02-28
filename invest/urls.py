from django.urls import path
from invest.views import HomeView, UserRegisterView, UserLoginView, UserLogoutView, ContactUsView, SelfImprovementDetailView,\
    InvestmentDetailView, BooksView, BookDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("users/register/", UserRegisterView.as_view(), name="user_register"),
    path("users/login/", UserLoginView.as_view(), name="login"),
    path("users/logout/", UserLogoutView.as_view(), name="logout"),
    path("contacts-us/", ContactUsView.as_view(), name="contacts_us"),
    path("selfimprovement/detail/", SelfImprovementDetailView.as_view(), name="selfimprovementdetail"),
    path("investment/detail/", InvestmentDetailView.as_view(), name="investment_detail"),
    path("books/", BooksView.as_view(), name="books"),
    path('books/<int:id>/', BookDetailView.as_view(), name="books_detail"),
]
