from django.db import models

# Create your models here.
class  subscribers(models.Model):
    name = models.CharField(max_length = 100, default="User")
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
