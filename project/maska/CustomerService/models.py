from django.db import models
from datetime import datetime

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city
        
class Flight(models.Model):
    origen = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.FloatField(default=3.0)
    traveile_time = models.DateField(default=datetime.now)
    bording_time = models.FloatField(default=0)
    landing_time = models.FloatField(default=0)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id}: {self.origen} to {self.destination} Duration: {self.duration} Hours  Travel Date: {self.traveile_time} Bording Time: {self.bording_time}  Landing Time: {self.landing_time} Price: {self.price} EGP"
