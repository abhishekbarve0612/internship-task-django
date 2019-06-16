from django.db import models
from django import forms
from task.models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = user
        fields = "__all__"

    def clean(self):
        cleaned_data = super(userForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match!!!"
            )
        
        """n =  user.objects.filter( name = user.name )
        if (n != 0 or e != 0):
            raise forms.ValidationError(
                "User with same name or email already exist!!!"
            )"""
        
        return cleaned_data

