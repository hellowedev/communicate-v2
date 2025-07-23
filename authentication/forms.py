from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserLoginForm(AuthenticationForm) :

    class Meta :
        model = User 
        fields = ('username', 'password')

class UserSignUpForm(UserCreationForm) :

    # A new field for email 
    email = forms.EmailField()
    class Meta :
        model = User 

        fields = ('username','email','password1','password2')