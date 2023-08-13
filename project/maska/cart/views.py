from django.shortcuts import render
def flights_cart(request):
    return render(request, 'pages/flights-cart.html')

def checkout (request):
    return render(request,"pages/checkout-form.html")
    

    
def Rating (request):
    return render(request,"pages/rating_submission.html")
    
