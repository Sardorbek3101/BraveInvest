from django.urls import path
from invest.views import HomeView, UserRegisterView, UserLoginView, UserLogoutView, ContactUsView, SelfImprovementDetailView,\
    InvestmentDetailView, BooksView, BookDetailView, AuthorView, ProfileView, BlackWindowView, BlackWindowDelView, AboutUsView, \
    AdminPageView, BookCreateView, AuthorCreateView, BookAuthorCreateView, BookUpdateView, BookDeleteView, AuthorUpdateView, \
    AuthorDeleteView, BookAuthorUpdateView, BookAuthorDeleteView

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
    path("books/author/update/<int:id>/", AuthorUpdateView.as_view(), name="author_update"),
    path("books/author/delete/<int:id>/", AuthorDeleteView.as_view(), name="author_delete"),
    path("books/book-author/update/<int:id>/", BookAuthorUpdateView.as_view(), name="b_a_update"),
    path("books/book-author/delete/<int:id>/", BookAuthorDeleteView.as_view(), name="b_a_delete"),
]
