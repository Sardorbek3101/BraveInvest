from django.shortcuts import redirect, render
from django.views import View
from invest.forms import UserCreateForm
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