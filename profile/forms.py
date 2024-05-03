"""Forms file for profile page"""
from django import forms
from .models import Profile


class UpdateImageForm(forms.ModelForm):
    """Class for image update form"""
    class Meta:
        model = Profile
        fields = ['image']
