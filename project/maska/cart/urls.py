from django.urls import path
from .import views
urlpatterns = [
 path('cart/', views.flights_cart, name='flight'),
]