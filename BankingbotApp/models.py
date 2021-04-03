from django.db import models

# Create your models here.
class register(models.Model):
    username =models.CharField(max_length=30)
    password =models.CharField(max_length=30)
    contact =models.CharField(max_length=13)
    email =models.CharField(max_length=30)
    address =models.CharField(max_length=40)