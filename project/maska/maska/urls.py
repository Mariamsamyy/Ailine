
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , include("home.urls")),
    path('flight/' , include("flight_options.urls")),
    path('registeration/' , include('registeration.urls')),
    path('', include('pages.urls')),
]
