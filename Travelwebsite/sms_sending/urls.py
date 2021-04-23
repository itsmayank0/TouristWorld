from django.urls import path
from . import views

urlpatterns = [
    path('sending_details/', views.sending_details, name="sending_details"),
]
