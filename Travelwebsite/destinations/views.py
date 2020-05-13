from django.shortcuts import render, redirect

# Create your views here.
def destination_page(request):
    return render(request, 'destinations.html')