from django.db import models
# Create your models here.


class Product(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    desc = models.TextField()
    model = models.CharField(max_length=200)


class Car(models.Model):
    name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=200)

