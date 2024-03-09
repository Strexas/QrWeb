from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


# Homepage
def home(request):
    return render(request, 'reg_sys/startpage.html')


# --Register a user
def register(request):
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
                return redirect('')
    context = {'form': form}
    return render(request, 'reg_sys/login.html', context=context)
