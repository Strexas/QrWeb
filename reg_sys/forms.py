# Here we will our model forms for users that want to register and login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Register a user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # Gives a nested namespace for configurations and keeps them in one place:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
