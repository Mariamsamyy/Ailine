from django.shortcuts import render, redirect
from .models import Comment
from .forms import RatingForm 
from .forms import Rating
from .models import Reservation
from .forms import FlightOrderForm,FlightOrder
from django.db.models import Count
from django.contrib import messages
# Create your views here.

def save_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        Comment.objects.create(name=name, comment=comment_text)
        
    return render(request, 'pages/contact_form.html')


def show_comments(request):
    comments = Comment.objects.all()
    return render(request, 'pages/comments_display.html', {'comments': comments})


def submit_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RatingForm()
    return render(request, 'pages/rating_submission.html', {'form': form})



def rating_display(request):
    ratings = Rating.objects.all()
    return render(request, 'pages/rating_display.html', {'ratings': ratings})

def trial(request):
    # to get the counts for edited and canceled reservations 
    canceled_count = Reservation.objects.filter(canceled=True).count()
    edited_count = Reservation.objects.filter(edited=True).count()

    return render(request, 'pages/trial.html', {'edited_count': edited_count,'canceled_count': canceled_count})

def order_flight(request):
    if request.method == 'POST':
        form = FlightOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight ordered successfully.')
            return redirect('order_flight')  
        else:
            messages.error(request, 'There was an error. Please check the form and try again.')

    else:
        form = FlightOrderForm()
    return render(request, 'pages/order_flight.html', {'form': form})

def most_ordered_flight(request):
    most_ordered_flight = FlightOrder.objects.values('flight_number').annotate(count=Count('flight_number')).order_by('-count').first()
    return render(request, 'pages/most_ordered_flight.html', {'most_ordered_flight': most_ordered_flight})

