from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AnimalApp.models import Animal, BuyerUser, SellerUser
from AnimalApp.serializers import AnimalSerializer, BuyerUserSerializer, SellerUserSerializer

from django.core.files.storage import default_storage

import uuid

# Create your views here.
### ANIMAL ###
@csrf_exempt
def animalApi(request, id=0):
    if request.method == 'GET':
        if (id == 0):
            animal = Animal.objects.all()
            animal_serializer = AnimalSerializer(animal, many=True)
            return JsonResponse(animal_serializer.data, safe=False)
        else:
            try:
                animal = Animal.objects.get(AnimalId = id)
            except:
                return JsonResponse("Animal Not Found", safe = False)
            animal_serializer = AnimalSerializer(animal, many = False)
            return JsonResponse(animal_serializer.data, safe = False)
    elif request.method == 'POST':
        animal_data=JSONParser().parse(request)
        animal_serializer = AnimalSerializer(data=animal_data)
        if animal_serializer.is_valid():
            animal_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add.", safe = False)
    elif request.method == 'PUT':
        animal_data = JSONParser().parse(request)
        animal = Animal.objects.get(AnimalId = animal_data['AnimalId'])
        animal_serializer = AnimalSerializer(animal, data=animal_data)
        if animal_serializer.is_valid():
            animal_serializer.save()
            return JsonResponse("Updated Successfully!", safe = False)
        return JsonResponse("Failed to Update.", safe = False)
    elif request.method == 'DELETE':
        animal = Animal.objects.get(AnimalId = id)
        animal.delete()
        return JsonResponse("Deleted Successfully!", safe = False)
    
    
### CUSTOMER USER ###
@csrf_exempt
def buyerUserApi(request, id=0):
    if request.method == 'GET':
        if (id != 0):
            try:
                buyerUser = BuyerUser.objects.get(BuyerUserId = id)
            except:
                return JsonResponse("Failed to find User", safe = False)
            buyerUser_serializer = BuyerUserSerializer(buyerUser, many=True)
            return JsonResponse(buyerUser_serializer.data, safe=False)
        else:
            return JsonResponse("Failed to retrieve User.", safe = False)
    elif request.method == 'POST':
        buyerUser_data=JSONParser().parse(request)
        buyerUser_serializer = BuyerUserSerializer(data=buyerUser_data)
        if buyerUser_serializer.is_valid():
            buyerUser_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add.", safe = False)
    elif request.method == 'PUT':
        buyerUser_data = JSONParser().parse(request)
        buyerUser = BuyerUser.objects.get(BuyerUserId = buyerUser_data['BuyerUserId'])
        buyerUser_serializer = BuyerUserSerializer(buyerUser, data=buyerUser_data)
        if buyerUser_serializer.is_valid():
            buyerUser_serializer.save()
            return JsonResponse("Updated Successfully!", safe = False)
        return JsonResponse("Failed to Update.", safe = False)
    elif request.method == 'DELETE':
        try:
            buyerUser = BuyerUser.objects.get(BuyerUserId = id)
        except:
            return JsonResponse("Failed to Delete.", safe = False)
        buyerUser.delete()
        return JsonResponse("Deleted Successfully!", safe = False)
    

### FILE SAVE ###
@csrf_exempt
def SaveFile(request):
    try:
        file = request.FILES['uploadedFile']
        unique_filename = str(uuid.uuid4())
        extension = str.split(file.name, '.')[1]
        unique_filename += '.' + extension
        file_name = default_storage.save(unique_filename, file)
        return JsonResponse(file_name, safe = False)
    except:
        return JsonResponse("Failed to Save File.", safe=False)

### DELETE FILE ###
@csrf_exempt
def DeleteFile(request):
    if request.method != 'DELETE':
        return JsonResponse("Invalid Request!", safe = False)
    try:
        request_data = JSONParser().parse(request)
        file_name = request_data['fileName']
        if default_storage.exists(file_name):
            default_storage.delete(file_name)
            return JsonResponse("File Deleted Successfully!", safe = False)
        else:
            return JsonResponse("No Such File.", safe = False)
    except:
        return JsonResponse("Failed to Delete File.", safe=False)