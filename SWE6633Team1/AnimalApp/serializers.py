from rest_framework import serializers
from AnimalApp.models2 import Animals, Appusers, Messages
#BuyerUser, SellerUser, Animals, AppUser

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = (
            'animal_id', 
            'animal_type', 
            'age',
            'name',
            'species',
            'gender',
            'size',
            'description',
            'photos',
            'email',
            'phone',
            'state',
            'country',
            'city',
            'postcode',
            'address1',
            'is_sold',
            'owner'
            )

class AppuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appusers
        fields = '__all__'
        # fileds = (
        #     'user_id',
        #     'first_name',
        #     'last_name',
        #     'location',
        #     'is_seller'
        # )

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        # fileds = (
        #     'message_id',
        #     'message_body',
        #     'receiver',
        #     'sender'
        # )