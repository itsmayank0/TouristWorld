from django.db import models

# Create your models here.
class destination(models.Model):
    img = models.ImageField(upload_to='pics')
    description = models.TextField() 
    price = models.IntegerField()
    title = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)
    reviews = models.IntegerField()

    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = 'Landing page destination'
        verbose_name_plural = 'Landing page destionations'

class SiteReview(models.Model):

    review = models.TextField()

class Testimonials(models.Model):

    customer_name = models.CharField(max_length=200)
    verified_review = models.TextField()

    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'


    def __str__(self):
        return self.customer_name
    
