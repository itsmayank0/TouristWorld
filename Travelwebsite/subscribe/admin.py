from django.contrib import admin
from .models import  subscribers
# Register your models here.
admin.site.register(subscribers)
admin.site.site_header = "TouristWorld Administration"