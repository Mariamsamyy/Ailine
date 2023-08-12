from django.shortcuts import render ,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .models import CUSTOMER
import json

# Create your views here.

def render_login (request):
    return render(request , 'registeration.html')

def render_signup (request):
    return render(request , 'registeration.html')

def render_forget_password (request):
    return render(request , 'registration/forgetpassword.html')




def handle_email_is_taken(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        user = CUSTOMER.objects.filter(email=email).first()
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
        
        new_user = CUSTOMER.objects.create(firstName=firstName,lastName=lastName,email=email, password=password,NationalId=NationalId)
        new_user.save()
      
        return redirect('home')
    else : return redirect('/registeration/signup')
    
def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get('emaill')
        pass1 = request.POST.get('passwordd')
        print("Email:", email)  # Print email for debugging
        print("Password:", pass1)  # Print password for debugging
        user = authenticate(request, username=email, password=pass1)
        print("User:", user)  # Print user object for debugging
        if user is not None:
           login(request, user)
           messages.success(request, 'You have been logged in.')
           return render(request, 'home/home.html')
        else:
           messages.success(request, 'error please try again.')
           return render(request, 'registeration.html')

    return render(request, 'registeration.html')  
 
def HomePage(request):
    return render(request, 'home/home.html')




