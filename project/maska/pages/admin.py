from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import Comment
from.models import Rating
from.models import Reservation
from.models import FlightOrder

# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reservation)
admin.site.register(FlightOrder)

