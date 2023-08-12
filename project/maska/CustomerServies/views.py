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
    
    return render(request,'CustomerServies/CustomerServies.html',{'Flights':flightFound})


def RoundTrip(request):
    if request.method == 'POST':
     Roundfrom=request.POST.get("RoundFrom")
     Roundto=request.POST.get("RoundTo")
     RoundReturnfrom=request.POST.get("RoundTo")
     RoundReturnTo=request.POST.get("RoundFrom")
     RoundDate=request.POST.get("RoundTravilingDate")
     
    flightFound = Flight.objects.all().filter(Roundorigen=Roundfrom, Rounddestination=Roundto,ReturnRoundorigen=RoundReturnfrom,ReturnRounddestination=RoundReturnTo,Roundtravil_date=RoundDate)
    
    return render(request,'CustomerServies/CustomerServies.html',{'Flights':flightFound})

def home(request):

   return render(request, 'home.html')

def render_login (request):
    return render(request , 'registration/login.html')

def render_signup (request):
    return render(request , 'registeration.html')

def render_forget_password (request):
    return render(request , 'registration/forgetpassword.html')

def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get('emaill')
        pass1 = request.POST.get('passwordd')
        user = authenticate(request, username=email, password=pass1)
        if User is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Wrong")

    return render(request, 'login.html')


def handle_email_is_taken(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        user = User.objects.filter(email=email).first()
        if user : return JsonResponse({"is_Taken" : True})
        else : return JsonResponse({"is_Taken" : False})
    else : return redirect('/registeration/signup')


def handle_signup_post (request):
    if request.method == 'POST':
        firstName= request.POST.get("fname")
        lastName= request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        NationalId = request.POST.get("nationalID")
        
        new_user = User.objects.create(firstName=firstName,lastName=lastName,email=email, password=password,NationalId=NationalId)
        new_user.save()
      
        return render(request , 'home.html',{'user': new_user}) # redirect home
    else : return redirect('/registeration/signup')
