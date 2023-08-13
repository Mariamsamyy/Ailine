from django.urls import path
from .import views
urlpatterns = [

path('checkout/', views.checkout, name='checkout'),
path('/rating_submission', views.Rating, name='Rating'),

]