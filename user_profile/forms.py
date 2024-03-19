from django import forms
from .models import Profile


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
