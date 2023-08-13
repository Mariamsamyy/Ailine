from django.shortcuts import render
from django.db.models import Q
from home.models import Airport
from home.models import Flight
from home.models import RoundFlight



# Create your views here.
def options(request):
    if request.method == 'POST':
      fromData = request.POST.get("From")
      toData = request.POST.get("To")
      TravilingDate=request.POST.get("date")
      flightFound = Flight.objects.all().filter(origen=fromData, destination=toData,travile_time=TravilingDate)
      
      print(fromData,toData)
    return render(request,'CustomerServies/CustomerServies.html',{'Flights':flightFound})


def RoundTrip(request):
    if request.method == 'POST':
      Roundfrom=request.POST.get("RoundFrom")
      Roundto=request.POST.get("RoundTo")
      RoundReturnfrom=request.POST.get("RoundTo")
      RoundReturnTo=request.POST.get("RoundFrom")
      RoundDate=request.POST.get("RoundTravilingDate")
      print(Roundfrom,Roundto,RoundReturnfrom,RoundReturnTo)
      RoundflightFound = RoundFlight.objects.all().filter(Roundorigen=Roundfrom, Rounddestination=Roundto,ReturnRoundorigen=RoundReturnfrom,ReturnRounddestination=RoundReturnTo,Roundtravil_date=RoundDate)
    return render(request,'CustomerServies/CustomerServies.html',{'ROUNDFlights':RoundflightFound})

