from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Check if email is taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        login(request, user)  # Automatically log in after registration
        return redirect('home')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home.html')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

