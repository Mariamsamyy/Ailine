from django.urls import path
from .import views

urlpatterns = [
    path('options/',views.options),
    # path('Round_trip/',views.Round_trip),
    
]
