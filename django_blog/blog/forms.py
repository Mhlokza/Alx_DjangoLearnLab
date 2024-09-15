from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustormCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        
