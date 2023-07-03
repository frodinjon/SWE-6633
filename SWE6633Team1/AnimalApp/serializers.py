from rest_framework import serializers
from AnimalApp.models2 import Animals
from AnimalApp.models2 import Appusers
from AnimalApp.models2 import Messages
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


class AppusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appusers
        feilds = (
            'user_id', 
            'first_name', 
            'last_name', 
            'location',
            'is_seller'
            )
        

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        feileds = (
            'message_id',
            'message_body',
            'receiver',
            'sender'
        )
        
# class SellerUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerUser
#         feilds = (
#             'SellerUserId', 
#             'SellerUserName', 
#             'SellerUserPassword', 
#             'SellerUserLocation'
#             )