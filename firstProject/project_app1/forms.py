from django.db import models
from django.forms import ModelForm, fields
from django import forms
from .models import RegisteredUser

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisteredUser
        fields = '__all__'