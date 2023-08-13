from django.shortcuts import render, HttpResponse, redirect
# from registeration.models import CUSTOMER,Login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def HomePage(request):
    return render(request, 'home/home.html')

def SignupPage(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        #backend validations
        if not fname or not lname or not email or not pass1 or not pass2:
            messages.error(request, 'All fields are required.')
            return render(request, 'registeration.html')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registeration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return render(request, 'registeration.html')

        # Create a new user
        my_user = User.objects.create_user(
            username=email, email=email, password=pass1, first_name=fname, last_name=lname)
        my_user.save()
        messages.success(request, 'You have successfully signed up.')
        return redirect('home')

    return render(request, 'registeration.html')

def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get('emaill')
        pass1 = request.POST.get('passwordd')
        print("Email:", email) 
        print("Password:", pass1)  
        user = authenticate(request, username=email, password=pass1)
        print("User:", user)  
        if user is not None:
           login(request, user)
           messages.success(request, 'You have been logged in.')
           return render(request, 'home/home.html')
        else:
           messages.success(request, 'error please try again.')
           return render(request, 'registeration.html')

    return render(request, 'registeration.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')