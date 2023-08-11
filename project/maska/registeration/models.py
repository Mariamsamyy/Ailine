from django.db import models

# Create your models here.
class User(models.Model):
    firstName=models.CharField(max_length = 30,default="")
    lastName= models.CharField(max_length = 30,default="")
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30) 
    NationalId=models.CharField(max_length = 30,default="")


def __str__(self):
    return self.email