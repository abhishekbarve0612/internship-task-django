from django.db import models
from django import forms

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=40)  
    email = models.EmailField()
    password = models.CharField(max_length = 20)  
    class Meta:  
        db_table = "users"  

