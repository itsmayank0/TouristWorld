from django.shortcuts import render
from .models import destination
# Create your views here.
def index(request):
    dest1 = destination()
    dest1.price = 860
    dest1.title = "Mumbai"
    dest1.img = "destination_1.jpg"
    dest1.description = 'This is the city of Dreams'
    dest2 = destination()
    dest2.price = 550
    dest2.img = "destination_2.jpg"
    dest2.title = "Goa"
    dest2.description = 'Go Goa Gone'
    dest3 = destination()
    dest3.img = "destination_3.jpg"
    dest3.price = 869
    dest3.title = "Hydrabad"
    dest3.description = 'I love Biryani'
    dests = [dest1,dest2,dest3]
    return render(request, 'index.html',{'dests': dests})