from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.save_comment, name='save_comment'),
    path('comments_display/', views.show_comments, name='show_comments'),
    path('submit_rating/', views.submit_rating, name='submit_rating'),
    path('rating_display/', views.rating_display, name='rating_display'),
    path('order_flight/', views.order_flight, name='order_flight'),
    path('most_ordered_flight/', views.most_ordered_flight, name='most_ordered_flight'), 
    path('trial/', views.trial, name='trial'),
    
]
