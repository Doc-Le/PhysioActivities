from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput
from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=200, label='Email')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name')
    password1 = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label='Password Confirmation', widget=forms.PasswordInput)
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
    