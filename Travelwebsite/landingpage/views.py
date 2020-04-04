from django.shortcuts import render,redirect
from .models import destination
# Create your views here.
def index(request):
    
    dests = destination.objects.all()
  
    return render(request, 'index.html',{'dests': dests})

# python manage.py runserver
def formsubmission(request):
    if request.method == 'GET':
        return render(request, 'adddest.html')
    else:
        img = request.POST['img']
        description = request.POST['description']
        price = request.POST['price']
        title = request.POST['title']
        offer = request.POST['offer']
        if offer=='no':
            offer=0
        else:
            offer=1
        reviews = request.POST['reviews']
        #images not uploaded here
        obj = destination(offer=offer,img=img, description=description,title=title,price=price,reviews=reviews)
        obj.save()
        return redirect('/')