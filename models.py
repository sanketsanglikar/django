from django.db import models

# Create your models here.

class Signup(models.Model):
    FullName = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Birthday = models.DateField(max_length=20)
    Gender = models.CharField(max_length=7)
    Email = models.EmailField(max_length=50)
    PhoneNumber = models.BigIntegerField()
    Designation = models.CharField(max_length=30)

