from django.db import models

# Create your models here.

class Product(models.Model) :
    name  =  models.CharField(max_length=100)
    des = models.TextField()
    price =  models.FloatField()
    created_at =  models.DateTimeField(auto_now_add=True)
    