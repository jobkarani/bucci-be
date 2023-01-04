from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = ImageField( manual_crop="")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name