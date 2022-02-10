from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100, help_text='First Name',label= 'First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name',label= 'First Name :')
    phone = forms.phoneField(max_length=200,label= 'Phone :')
    location = forms.locationField(max_length=200,label= 'Location :')
    
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }

