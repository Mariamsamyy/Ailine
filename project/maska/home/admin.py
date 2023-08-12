from django.contrib import admin
from home.models import Flight,Airport,RoundFlight

admin.site.register(Airport)



class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destination', 'Price', 'duration','travile_time')
    list_filter = ('origen', 'destination', 'Price')
    search_fields = ('origen', 'destination', 'Price')

admin.site.register(Flight, FlightAdmin)

class RoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'Roundorigen', 'Rounddestination', 'RoundPrice', 'Roundduration','Roundtravil_date')
    list_filter = ('Roundorigen', 'Rounddestination', 'RoundPrice')
    search_fields = ('Roundorigen', 'Rounddestination', 'RoundPrice')

admin.site.register(RoundFlight, RoundAdmin)

