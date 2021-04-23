from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.info(request, "See You Later Bye 🙋‍♂️")
    return redirect('/')