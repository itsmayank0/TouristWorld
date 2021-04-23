from django.urls import path
from . import views

urlpatterns = [
    path('destination_page', views.destination_page, name="destination_page")
]
