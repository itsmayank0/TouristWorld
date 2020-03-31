from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User

# Create your views here.

def register(request):
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,'exist.html', {'message':'Username is alredy exist!'})

            elif User.objects.filter(email=email).exists():
                return render(request,'exist.html', {'message':'Email already exists!'})
                print("email esist")
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)        
                user.save()
                print("userCreated..")
                return render(request,'exist.html', {'message':'User created!'})
        else:
            print("Specify same password")
            return render(request,'exist.html', {'message':'Passwords dont match!'})
        
    else:    
        return render(request, 'signup.html')

