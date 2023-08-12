from django.contrib import admin
from.models import Comment
from.models import Rating
from.models import Reservation
from.models import FlightOrder
from.models import CustomPermission
from.models import CustomUser
# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Reservation)
admin.site.register(FlightOrder)
admin.site.register(CustomPermission)
admin.site.register(CustomUser)



