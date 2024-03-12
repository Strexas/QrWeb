"""Here we will our model forms for users that want to register and login"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class UserRegisterForm(UserCreationForm):
    """
    Form class for user registration.

    Inherits from:
    - UserCreationForm: Django's built-in form for user creation.

    Attributes:
    - email: An EmailField for the user's email address.
    - Meta: Inner class specifying metadata for the form.
        - model: Model class to be used for the form, which is obtained using get_user_model().
        - fields: Fields in the form, including 'username', 'email', 'password1', and 'password2'.
    """
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """
    Form class for user login.

    Inherits from:
    - AuthenticationForm: Django's built-in form for user authentication.

    Attributes:
    - username: A CharField representing the username field.
                It uses a TextInput widget for input.
    - password: A CharField representing the password field.
                It uses a PasswordInput widget for input.
    """
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
