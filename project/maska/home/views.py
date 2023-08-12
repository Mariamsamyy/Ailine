from django.shortcuts import render
from home.models import Airport
# Create your views here.
def home(request):
    return render(request,'home/home.html',{'Airport':Airport.objects.all})

