
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/' , include("cart.urls")),
    path('' , include("home.urls"), name='home'),
    path('flight/' , include("CustomerServies.urls")),    path('registeration/' , include('registeration.urls')),
    path('pages/', include('pages.urls')),


]
