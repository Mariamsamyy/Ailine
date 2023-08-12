from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    rating_value = models.PositiveIntegerField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    # ... existing fields ...
    canceled = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    edited_timestamp = models.DateTimeField(null=True, blank=True)

class FlightOrder(models.Model):
    flight_number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

