from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    rating_value = models.PositiveIntegerField()
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



# models.py
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # ... other fields ...

    # Customize related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_set')

    # ... other fields ...

    # Add any additional fields or methods you need


from django.contrib.auth.models import Permission

class CustomPermission(models.Model):
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE, primary_key=True)
    # ... additional fields ...

    class Meta:
        verbose_name = 'Custom Permission'
        verbose_name_plural = 'Custom Permissions'



