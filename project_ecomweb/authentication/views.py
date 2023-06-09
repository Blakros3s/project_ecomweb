from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You're Logged In !")
            return redirect('dashboard')
        return redirect('login')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        return redirect('register')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You've Successfully Logged Out!")
        return redirect('login')