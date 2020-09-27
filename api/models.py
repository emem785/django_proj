from django.db import models

# Create your models here.

class User(models.Model):
    firebase_key = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20,unique=True)    
