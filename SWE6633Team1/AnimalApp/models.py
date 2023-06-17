from django.db import models

# Create your models here.

class Animal(models.Model):
    AnimalId = models.AutoField(primary_key=True)
    AnimalName = models.CharField(max_length=100)
    AnimalBreed = models.CharField(max_length=100)


class BuyerUser(models.Model):
    BuyerUserId = models.AutoField(primary_key=True)
    BuyerUserName = models.CharField(max_length=100)
    BuyerUserPassword = models.CharField(max_length=100)
    BuyerUserLocation = models.IntegerField()


class SellerUser(models.Model):
    SellerUserId = models.AutoField(primary_key=True)
    SellerUserName = models.CharField(max_length=100)
    SellerUserPassword = models.CharField(max_length=100)
    SellerUserLocation = models.IntegerField()

