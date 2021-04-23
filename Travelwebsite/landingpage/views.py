from django.shortcuts import render,redirect
from .models import destination,Testimonials


def index(request):
    dests = destination.objects.all()
    testimonials = Testimonials.objects.all()
    offer_count = 0
    test_count = 0
    for i,j in zip(dests,testimonials):
        if i.offer:
            offer_count +=1
        if j.verified_review:
            test_count +=1
    return render(request, 'index.html',{'dests': dests, 'offer_count': offer_count, 'testimonials': testimonials, 'test_count': test_count})

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