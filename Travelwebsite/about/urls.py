from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name="Team Members"),
    path('about/', views.team, name="Team Members")
]
