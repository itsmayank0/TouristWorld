from django.urls import path
from . import views

urlpatterns = [
    path('subscribe_details', views.subscribe_details, name="details")
]
