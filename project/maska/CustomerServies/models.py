
from django.db import models



class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.message}"
    
class User(models.Model):
    firstName=models.CharField(max_length = 30,default="")
    lastName= models.CharField(max_length = 30,default="")
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30) 
    NationalId=models.CharField(max_length = 30,default="")


def __str__(self):
    return self.email
    


