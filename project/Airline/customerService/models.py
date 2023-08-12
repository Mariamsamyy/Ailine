from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from datetime import datetime


class Passenger(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField( max_length=20, null=False)
    username = models.CharField(max_length=30, null=False, default=None)
    email = models.EmailField(null=False)
    nationalId = models.IntegerField()
    
    def __str__(self):
        return f"id {self.id}, name:{self.firstname} {self.lastname}, email:{self.email}"

class Airport(models.Model):
    
    code= models.CharField(max_length=3,null=False)
    city= models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.city
        
class Flight(models.Model):
    origen = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='Depature', default=None, null=False)
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='to', default=None, null=False)
    duration = models.FloatField(default=3.0)
    travile_time = models.DateField(default=datetime.now)
    BordingTime = models.FloatField(default=0)
    LandingTime = models.FloatField(default=0)
    Price = models.IntegerField(default=0)
    passanger = getattr(Passenger,'firtname','lastname')

    def __str__(self):
        return f"{self.id}: {self.origen} to {self.destination} Duration: {self.duration} Hours  Travile Date: {self.travile_time} Bording Time: {self.BordingTime}  Landing Time: {self.LandingTime} Price: {self.Price} EGP"
            
class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


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
    
#class CustomerServiceUser():

class RoundFlight(models.Model):
    Roundorigen = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='RoundDepature')
    Rounddestination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='Roundto')
    ReturnRoundorigen = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='RoundReturnDepature')
    ReturnRounddestination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='RoundReturnto')
    Roundduration = models.FloatField(default=6.0)
    Roundtravil_date = models.DateField(default=datetime.now)
    RoundBordingTime= models.FloatField(default=0)
    RoundLandingTime= models.FloatField(default=0)
    ReturnRoundBordingTime= models.FloatField(default=0)
    ReturnRoundLandingTime= models.FloatField(default=0)
    RoundPrice=models.IntegerField(default=0)
    # def __str__(self):
    #     return f"{self.id}: {self.Roundorigen} to {self.Rounddestination} Duration: {self.duration} Hours  Travile Date: {self.travile_time} Bording Time: {self.BordingTime}  Landing Time: {self.LandingTime} Price: {self.Price} EGP"