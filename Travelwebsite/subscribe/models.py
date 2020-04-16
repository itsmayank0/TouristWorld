from django.db import models

# Create your models here.
class  subscribers(models.Model):
    name = models.CharField(max_length = 100, default="User")
    email = models.EmailField()
    
