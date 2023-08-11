from django.shortcuts import render
from django.db.models import Q
# from home.models import Airport
# from home.models import Flight

# # Create your views here.
# def options(request):
#     if request.method == 'POST':
#       fromData = request.POST.get("From")
#       toData = request.POST.get("To")
#       TravilingDate=request.POST.get("date")
#       flightFound = Flight.objects.all().filter(origen=fromData, destination=toData,travile_time=TravilingDate)
    
#     return render(request,'flight_options/flight_options.html',{'Flights':flightFound})


# def Round_trip(request):
#       if request.method == 'POST':
#         fromData = request.POST.get("RoundFrom")
#         toData = request.POST.get("RoundTo")
#         TravilingDate=request.POST.get("RoundTravilingDate")
#         DurationData=request.POST.get("RoundDuration")
#         Passengersnum=request.POST.get("Passangers")
#         flightFound = Flight.objects.filter(
#         Q(origen=fromData, destination=toData, travile_time=TravilingDate) &
#         Q(origen=toData, destination=fromData))
            
#       return render(request,'flight_options/flight_options.html',{'Flights':flightFound})
        
  
      
        
