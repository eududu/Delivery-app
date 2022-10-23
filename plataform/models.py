from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    district = models.CharField(max_length=50)
    complement = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=8)
