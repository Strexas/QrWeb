"""Here we will our model forms for users that want to register and login"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Register a user
class UserRegisterForm(UserCreationForm): # pylint: disable=too-many-ancestors
    """UserRegister form"""
    email = forms.EmailField()

    class Meta:  # Gives a nested namespace for configurations and keeps them in one place:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


# Login a user
class LoginForm(AuthenticationForm):
    """LoginForm"""
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
