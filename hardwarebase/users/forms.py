from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'pwd_hash']


class LoginForm(forms.Form):
    userid = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8)