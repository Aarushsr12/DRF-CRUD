from django.db import models

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
