from django.db import models

# Create your models here.
class destinations(models.Model):
    title = models.CharField(primary_key=True, max_length=2000)
    description = models.TextField()
    destionation_image = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
    price = models.IntegerField(blank=True)
    feature1 = models.TextField(blank=True)
    feature2= models.TextField(blank=True)
    feature3 = models.TextField(blank=True)
    feature4 = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)+str(self.price)

    class Meta:
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'