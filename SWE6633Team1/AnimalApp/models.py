from django.db import models

# from SWE6633Team1.AnimalApp.models2 import Animals

# Create your models here.
# class AppUser(models.Model):
#     app_user_id = models.AutoField(primary_key=True)
#     user_first_name = models.CharField(max_length=100)
#     user_last_name = models.CharField(max_length=100)
#     user_location = models.IntegerField()
#     user_is_seller = models.BooleanField()


# class Animals(models.Model):
#     animal_id = models.AutoField(primary_key=True)
#     animal_type = models.CharField(max_length=255)
#     age = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     species = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#     size = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     photos = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     postcode = models.CharField(max_length=255)
#     address1 = models.CharField(max_length=255)
#     class Meta:
#         managed = False
#         db_table = 'animals'
    # is_sold = models.BooleanField(null = True, blank = True)
    # animal_owner_id = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, related_name="owner", blank = True)


# class BuyerUser(models.Model):
#     BuyerUserId = models.AutoField(primary_key=True)
#     BuyerUserName = models.CharField(max_length=100)
#     BuyerUserPassword = models.CharField(max_length=100)
#     BuyerUserLocation = models.IntegerField()


# class SellerUser(models.Model):
#     SellerUserId = models.AutoField(primary_key=True)
#     SellerUserName = models.CharField(max_length=100)
#     SellerUserPassword = models.CharField(max_length=100)
#     SellerUserLocation = models.IntegerField()


# class Message(models.Model):
#     MessageId = models.AutoField(primary_key=True)
#     MessageSenderId = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, related_name="message_sender_id")
#     MessageReceiverId = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, related_name="message_receiver_id")
#     IsRead = models.BooleanField(blank=False)
#     MessageBody = models.CharField(max_length=50000)


    