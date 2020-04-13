from django.db import models

# Create your models here.
class destination(models.Model):
    img = models.ImageField(upload_to='pics')
    description = models.TextField() 
    price = models.IntegerField()
    title = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)
    reviews = models.IntegerField()

class SiteReview(models.Model):

    review = models.TextField()
    
