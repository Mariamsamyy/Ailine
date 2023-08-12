from django.shortcuts import render, redirect
from .models import Comment
from .forms import RatingForm # Import the RatingForm from forms.py
from .forms import Rating
from .models import Reservation
from .forms import FlightOrderForm,FlightOrder
from django.db.models import Count
from django.contrib import messages
# Create your views here.

def save_comment(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        
        # Save the comment to the database
        Comment.objects.create(name=name, comment=comment_text)
        
    # Render the contact form (regardless of whether the request method is POST or not)
    return render(request, 'pages/contact_form.html')


def show_comments(request):
    # Get all comments from the database
    comments = Comment.objects.all()
    return render(request, 'pages/comments_display.html', {'comments': comments})




def submit_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_display')  # Assuming you have a URL named 'rating_display'
    else:
        form = RatingForm()
    return render(request, 'pages/rating_submission.html', {'form': form})



def rating_display(request):
    ratings = Rating.objects.all()
    return render(request, 'pages/rating_display.html', {'ratings': ratings})

def canceled_reservations(request):
    canceled_count = Reservation.objects.filter(canceled=True).count()
    return render(request, 'pages/canceled_reservations.html', {'canceled_count': canceled_count})

def edited_reservations(request):
    edited_count = Reservation.objects.filter(edited=True).count()
    return render(request, 'pages/edited_reservations.html', {'edited_count': edited_count})

def trial(request):
    # Get the counts for edited and canceled reservations (replace with your actual logic)
    canceled_count = Reservation.objects.filter(canceled=True).count()
    edited_count = Reservation.objects.filter(edited=True).count()

    return render(request, 'pages/trial.html', {'edited_count': edited_count,'canceled_count': canceled_count})

def order_flight(request):
    if request.method == 'POST':
        form = FlightOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight ordered successfully.')
            return redirect('order_flight')  # Redirect to the same page (PRG pattern)
        else:
            # If the form is not valid, you can also add an error message
            messages.error(request, 'There was an error. Please check the form and try again.')

    else:
        form = FlightOrderForm()
    return render(request, 'pages/order_flight.html', {'form': form})


def most_ordered_flight(request):
    most_ordered_flight = FlightOrder.objects.values('flight_number').annotate(count=Count('flight_number')).order_by('-count').first()
    return render(request, 'pages/most_ordered_flight.html', {'most_ordered_flight': most_ordered_flight})


