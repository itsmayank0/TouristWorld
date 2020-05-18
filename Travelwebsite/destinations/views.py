from django.shortcuts import render, redirect
from django.contrib import messages
from .models import destinations
# Create your views here.


def destination_page(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please Login to access Destionations!")
        return redirect("/signin/signin")
    else:
        dests = destinations.objects.all()
        return render(request, 'destinations.html', {'dests': dests})