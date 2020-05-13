from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages 

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
                messages.info(request,"Username Already exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)        
                user.save()
                messages.info(request,"User Successfully created account")
                return redirect('/signin/signin')
                # return render(request,'exist.html', {'message':'User created!'})
        else:
            messages.info(request, "Password Dont match")
            return redirect('register')
            # return render(request,'exist.html', {'message':'Passwords dont match!'})
        
    else:    
        return render(request, 'signup.html')

