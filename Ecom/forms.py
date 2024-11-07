from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length= 100 , required=True)
    last_name = forms.CharField(max_length= 100 , required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')