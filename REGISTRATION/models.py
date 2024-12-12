from django.db import models

# Create your models here.

class Divers(models.Model):
    name = models.CharField(max_length=255)
    availability = models.IntegerChoices(min=0, max=3)


class Clients(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    length = models.IntegerField(max_value=250)
    weight = models.IntegerField(max_value=140)
    age = models.IntegerField(min_value=14,max_value=100)


class Sesja(models.model):
    pass