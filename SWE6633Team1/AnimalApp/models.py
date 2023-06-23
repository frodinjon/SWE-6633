from django.db import models

from users.models import User

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


class Message(models.Model):
    MessageId = models.AutoField(primary_key=True)
    MessageSenderId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="message_sender_id")
    MessageReceiverId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="message_receiver_id")
    IsRead = models.BooleanField(blank=False)
    MessageBody = models.CharField(max_length=50000)