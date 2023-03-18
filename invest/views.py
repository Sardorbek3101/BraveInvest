from django.shortcuts import redirect, render
from django.views import View
from .models import Book, Author
from invest.forms import UserCreateForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    
class UserRegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, "users/register.html", {"form":form})
    
    def post(self, request):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "users/register.html", {"form":form})
        messages.success(request, "You have successfully registered")
        return redirect('home')


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form":form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            return render(request, "users/login.html", {"form":login_form})
        

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("home")


class ContactUsView(View):
    def get(self, request):
        return render(request, "contacts_us.html")
    

class AboutUsView(View):
    def get(self, request):
        return render(request, "about_us.html")
    

class SelfImprovementDetailView(View):
    def get(self, request):
        return render(request, "selfimprovementdetail.html")


class InvestmentDetailView(View):
    def get(self, request):
        return render(request, "investment_detail.html")
    

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        search = request.GET.get("q", "")
        if search:
            books = books.filter(title__icontains=search)
        pagenator = Paginator(books, 4)
        page_num = request.GET.get("page", 1)
        books_page = pagenator.get_page(page_num)
        return render(request, "books.html", {"books":books_page, "search":search})
    

class BookDetailView(View):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except:
            messages.warning(request, "По вашему запросу книг не найдено")
            return redirect("books")
        return render(request, "book_detail.html", {"book":book})


class AuthorView(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        return render(request, "author.html", {"author":author})
    

class ProfileView(View):
    def get(self, request):
       user = request.user
       return render(request, "profile.html", {"user":user})


class BlackWindowView(View):
    def post(self, request):
        if request.user.is_authenticated:
            path = request.POST['path']
            request.user.black_theme = True
            request.user.save()
            return redirect(path)
        else:
            return redirect("login") 
    

class BlackWindowDelView(View):
    def post(self, request):
        if request.user.is_authenticated:
            path = request.POST['path']
            print(path)
            print('salom')
            request.user.black_theme = False
            request.user.save()
            return redirect(path)
        else:
            return redirect("login") 