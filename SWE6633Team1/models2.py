# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Animals(models.Model):
    animal_id = models.AutoField(primary_key=True)
    animal_type = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    photos = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    is_sold = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey('Appusers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animals'


class Appusers(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    is_seller = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'appUsers'


class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_body = models.TextField()
    receiver = models.ForeignKey(Appusers, models.DO_NOTHING, blank=True, null=True)
    sender = models.ForeignKey(Appusers, models.DO_NOTHING, related_name='messages_sender_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'
