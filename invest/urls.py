from django.urls import path
from invest.views import HomeView, UserRegisterView, UserLoginView, UserLogoutView, ContactUsView, SelfImprovementDetailView,\
    InvestmentDetailView, BooksView, BookDetailView, AuthorView, ProfileView, BlackWindowView, BlackWindowDelView, AboutUsView, \
    AdminPageView, BookCreateView, AuthorCreateView, BookAuthorCreateView, BookUpdateView, BookDeleteView

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
    path("books/author/<int:id>/", AuthorView.as_view(), name="author"),
    path("users/profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("users/black/window/activate/", BlackWindowView.as_view(), name="black_window"),
    path("users/black/window/deactivate/", BlackWindowDelView.as_view(), name="black_window_del"),
    path("about/us/", AboutUsView.as_view(), name="about_us"),  
    path("users/staff/page/", AdminPageView.as_view(), name="admin_page"), 
    path("books/create/", BookCreateView.as_view(), name="book_create"),
    path("books/author/create/", AuthorCreateView.as_view(), name="author_create"),
    path("books/book-author/create/", BookAuthorCreateView.as_view(), name="b_a_create"),
    path("books/update/<int:id>/", BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:id>/", BookDeleteView.as_view(), name="book_delete"),
]
