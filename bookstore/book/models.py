# from django.db import models

# # Create your models here.
# book/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
