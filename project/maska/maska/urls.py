
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/' , include("cart.urls")),
    path('home/' , include("home.urls"), name='home'),

    path('flightt/' , include("CustomerServies.urls")),

    # path('flight/' , include("flight_options.urls")),

    path('registeration/' , include('registeration.urls')),

    
    path('', include('pages.urls')),


]
