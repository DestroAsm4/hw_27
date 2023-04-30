from django.db import models
import csv

class ADS(models.Model):

    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField()

class Categories(models.Model):

    name = models.CharField(max_length=30)




# Create your models here.
