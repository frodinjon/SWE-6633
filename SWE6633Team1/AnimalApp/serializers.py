from rest_framework import serializers
from AnimalApp.models import BuyerUser, SellerUser, animals

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = animals
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
            'address1'
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