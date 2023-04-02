from django.shortcuts import redirect, render
from django.views import View
from .models import Book, Author, User, BookAuthor
from invest.forms import UserCreateForm, BookCreateForm, AuthorCreateForm, BookAuthorCreateForm
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
    def get(self, request, id):
       user = User.objects.get(id=id)
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


class AdminPageView(View):
    def get(self, request):
        if request.user.is_staff:
            get_table = request.GET.get("table", "users")
            del_book = None
            del_author = None
            del_b_a = None
            book_del_id = request.GET.get("delete-book", "")
            author_del_id = request.GET.get("delete-author", "")
            b_a_del_id = request.GET.get("delete-book-author", "")
            if book_del_id:
                try:
                    del_book = Book.objects.get(id=book_del_id)
                except:
                    messages.warning(request, "No books found matching your search")
            
            if author_del_id:
                try:
                    del_author = Author.objects.get(id=author_del_id)
                except:
                    messages.warning(request, "No authors found matching your search")

            if b_a_del_id:
                try:
                    del_b_a = BookAuthor.objects.get(id=b_a_del_id)
                except:
                    messages.warning(request, "No book authors found matching your search")

            if get_table == "users":
                table = User.objects.all()
                table_value = "users"
            elif get_table == "books":
                table = Book.objects.all()
                table_value = "books"
            elif get_table == "authors":
                table = Author.objects.all()
                table_value = "authors"
            elif get_table == "book_authors":
                table = BookAuthor.objects.all()
                table_value = "book_authors"
            else:
                table = ""
                table_value = ""
            return render(request, "admin_page.html", {"table":table, "table_value":table_value, "del_book":del_book, "del_author":del_author, "del_b_a":del_b_a})
        else:
            return redirect("home")
        

class BookCreateView(View):
    def get(self, request):
        if request.user.is_staff:
            book_form = BookCreateForm()
            return render(request, "book_create.html", {"form":book_form})
        return redirect("home")
    
    def post(self, request):
        if request.user.is_staff:
            book_form = BookCreateForm(data=request.POST, files=request.FILES)
            if book_form.is_valid():
                book_form.save()
                return redirect("admin_page")
            return render(request, "book_create.html", {"form":book_form})
        return redirect("home")
    

class BookUpdateView(View):
    def get(self, request, id):
        if request.user.is_staff:
            book = Book.objects.get(id=id)
            book_form = BookCreateForm(instance=book)
            return render(request, "book_update.html", {"form":book_form})
        return redirect("home")
    
    def post(self, request, id):
        if request.user.is_staff:
            book = Book.objects.get(id=id)
            book_form = BookCreateForm(instance=book, data=request.POST, files=request.FILES)
            if book_form.is_valid():
                book_form.save()
                return redirect("admin_page")
            else:
                return render(request, "book_update.html", {"form":book_form})
        return redirect("home")
    

class BookDeleteView(View):
    def post(self, request, id):
        if request.user.is_staff:
            book = Book.objects.get(id=id)
            book.delete()
            return redirect("admin_page")
        return redirect("home")


class AuthorCreateView(View):
    def get(self, request):
        if request.user.is_staff:
            author_form = AuthorCreateForm()
            return render(request, "author_create.html", {"form":author_form})
        return redirect("home")
    
    def post(self, request):
        if request.user.is_staff:
            author_form = AuthorCreateForm(data=request.POST, files=request.FILES)
            if author_form.is_valid():
                author_form.save()
                return redirect("admin_page")
            return render(request, "author_create.html", {"form":author_form})
        return redirect("home")
    

class AuthorUpdateView(View):
    def get(self, request, id):
        if request.user.is_staff:
            author = Author.objects.get(id=id)
            author_form = AuthorCreateForm(instance=author)
            return render(request, "author_update.html", {"form":author_form})
        return redirect("home")
    
    def post(self, request, id):
        if request.user.is_staff:
            author = Author.objects.get(id=id)
            author_form = AuthorCreateForm(instance=author, data=request.POST, files=request.FILES)
            if author_form.is_valid():
                author_form.save()
                return redirect("admin_page")
            else:
                return render(request, "author_update.html", {"form":author_form})
        return redirect("home")


class AuthorDeleteView(View):
    def post(self, request, id):
        if request.user.is_staff:
            author = Author.objects.get(id=id)
            author.delete()
            return redirect("admin_page")
        return redirect("home")


class BookAuthorCreateView(View):
    def get(self, request):
        if request.user.is_staff:
            b_a_form = BookAuthorCreateForm()
            return render(request, "b_a_create.html", {"form":b_a_form})
        return redirect("home")
    
    def post(self, request):
        if request.user.is_staff:
            b_a_form = BookAuthorCreateForm(data=request.POST)
            if b_a_form.is_valid():
                b_a_form.save()
                return redirect("admin_page")
            return render(request, "b_a_create.html", {"form":b_a_form})
        return redirect("home")


class BookAuthorUpdateView(View):
    def get(self, request, id):
        if request.user.is_staff:
            b_a = BookAuthor.objects.get(id=id)
            b_a_form = BookAuthorCreateForm(instance=b_a)
            return render(request, "b_a_update.html", {"form":b_a_form})
        return redirect("home")
    
    def post(self, request, id):
        if request.user.is_staff:
            b_a = BookAuthor.objects.get(id=id)
            b_a_form = BookAuthorCreateForm(instance=b_a, data=request.POST, files=request.FILES)
            if b_a_form.is_valid():
                b_a_form.save()
                return redirect("admin_page")
            else:
                return render(request, "b_a_update.html", {"form":b_a_form})
        return redirect("home")
    

class BookAuthorDeleteView(View):
    def post(self, request, id):
        if request.user.is_staff:
            b_a = BookAuthor.objects.get(id=id)
            b_a.delete()
            return redirect("admin_page")
        return redirect("home")