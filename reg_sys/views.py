"""views.py"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LoginForm
# Create your views here.


def home(request):
    """Homepage"""
    return render(request, 'reg_sys/startpage.html')


# --Register a user
def register(request):
    """Registration process"""
    if request.method == 'POST':  # Checking if we are sending data to database
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saving a user
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'reg_sys/register.html', context=context)


# - Login a user
def user_login(request):
    """Login process"""
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, f'{form.cleaned_data["username"]} successfully logged in')
            if user is not None:
                auth.login(request, user)
                return redirect('profile')
    context = {'form': form}
    return render(request, 'reg_sys/login.html', context=context)


# - User logout
def user_logout(request):
    """Logout process"""
    auth.logout(request)
    return redirect('login')


# - Profile page
@login_required(login_url='login')
def user_profile(request):
    """Registration process"""
    return render(request, 'reg_sys/profile.html')
