from django.urls import path
from . import views

#Demo form submission

urlpatterns = [
    path('', views.index, name='index'),
    path('addDestination/formsubmission', views.formsubmission, name="formsubmission"),
    path('addDestination/', views.formsubmission, name="pade")
]