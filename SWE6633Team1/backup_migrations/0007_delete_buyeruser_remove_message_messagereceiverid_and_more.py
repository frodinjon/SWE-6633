# Generated by Django 4.2.2 on 2023-07-01 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnimalApp', '0006_alter_animals_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuyerUser',
        ),
        migrations.RemoveField(
            model_name='message',
            name='MessageReceiverId',
        ),
        migrations.RemoveField(
            model_name='message',
            name='MessageSenderId',
        ),
        migrations.DeleteModel(
            name='SellerUser',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
