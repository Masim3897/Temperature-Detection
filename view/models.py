from django.db import models
class Temprature(models.Model):
    
    name = models.CharField(max_length = 500)
    value =models.FloatField()


# Create your models here.
