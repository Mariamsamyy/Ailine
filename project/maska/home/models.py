from django.db import models
from django.utils import timezone
from datetime import datetime

class Airport(models.Model):
    
    code= models.CharField(max_length=3)
    city= models.CharField(max_length=50)
    
    def __str__(self):
        return self.city
        
class Flight(models.Model):
    origen = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='Depature')
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='to')
    duration = models.FloatField(default=3.0)
    travile_time = models.DateField(default=datetime.now)
    BordingTime= models.FloatField(default=0)
    LandingTime= models.FloatField(default=0)
    Price=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id}: {self.origen} to {self.destination} Duration: {self.duration} Hours  Travile Date: {self.travile_time} Bording Time: {self.BordingTime}  Landing Time: {self.LandingTime} Price: {self.Price} EGP"

