from rest_framework import serializers
from AnimalApp.models import BuyerUser, SellerUser, Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            'AnimalId', 
            'AnimalName', 
            'AnimalBreed'
            )


class BuyerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerUser
        feilds = (
            'BuyerUserId', 
            'BuyerUserName', 
            'BuyerUserPassword', 
            'BuyerUserLocation'
            )
        
class SellerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerUser
        feilds = (
            'SellerUserId', 
            'SellerUserName', 
            'SellerUserPassword', 
            'SellerUserLocation'
            )