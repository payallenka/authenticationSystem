# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name or path
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def home(request):
    return render(request, 'accounts/home.html')


def user_list(request):
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'accounts/user.html', {'users': users})