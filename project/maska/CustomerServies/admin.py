from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Login,Flight,Airport,ContactForm ,Passenger

admin.site.register(Login)
#admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(ContactForm)
admin.site.register(Passenger)
admin.site.register(Flight)
#admin.site.register(FlightAdmin)


