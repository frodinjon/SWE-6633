from rest_framework import viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AnimalApp.models2 import Animals
from AnimalApp.serializers import AnimalSerializer
# from AnimalApp.models import Animals, BuyerUser, SellerUser
# from AnimalApp.serializers import AnimalSerializer, BuyerUserSerializer, SellerUserSerializer

from django.core.files.storage import default_storage

import uuid

def response_helper(success, message="", data=0):
    return {
        "success": success,
        "message": message,
        "data": data
    }

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# Create your views here.
### ANIMAL ###
@csrf_exempt
def animalApi(request, id=0):
    if request.method == 'GET':
        if (id == 0):
            animal = Animals.objects.all()
            animal_serializer = AnimalSerializer(animal, many=True)
            return JsonResponse(data = response_helper(True, "", animal_serializer.data), safe=False)
        else:
            try:
                animal = Animals.objects.get(animal_id = id)
            except:
                return JsonResponse(data = response_helper(False, "Animal Not Found"), safe = False)
            animal_serializer = AnimalSerializer(animal, many = False)
            return JsonResponse(data = response_helper(True, "", animal_serializer.data), safe = False)
    elif request.method == 'POST':
        animal_data=JSONParser().parse(request)
        animal_serializer = AnimalSerializer(data=animal_data)
        if animal_serializer.is_valid():
            try:
                animal_serializer.save()
            except:
                return JsonResponse(data = response_helper(False, "Failed to Save. Please Try Again"), safe=False)
            #On Successful Save
            return JsonResponse(data = response_helper(True, "Added Successfully"), safe = False)
        return JsonResponse(data = response_helper(False, "Failed to Add"), safe = False)
    elif request.method == 'PUT':
        animal_data = JSONParser().parse(request)
        animal = Animals.objects.get(animal_id = animal_data['animal_id'])
        animal_serializer = AnimalSerializer(animal, data=animal_data)
        if animal_serializer.is_valid():
            try:
                animal_serializer.save()
                return JsonResponse(data = response_helper(True, "Updated Successfully!"), safe = False)
            except:
                return JsonResponse(data = response_helper(False, "Failed to Save. Please Try Again."), safe=False)
        return JsonResponse(data = response_helper(False, "Failed to Update."), safe = False)
    elif request.method == 'DELETE':
        try:
            animal = Animals.objects.get(animal_id = id)
            animal.delete()
            return JsonResponse(data=response_helper(True, "Deleted Successfully!"), safe = False)
        except:
            return JsonResponse(data=response_helper(False, "Failed to Delete"), safe=False)
    
    
# ### CUSTOMER USER ###
# @csrf_exempt
# def buyerUserApi(request, id=0):
#     if request.method == 'GET':
#         if (id != 0):
#             try:
#                 buyerUser = BuyerUser.objects.get(BuyerUserId = id)
#             except:
#                 return JsonResponse("Failed to find User", safe = False)
#             buyerUser_serializer = BuyerUserSerializer(buyerUser, many=True)
#             return JsonResponse(buyerUser_serializer.data, safe=False)
#         else:
#             return JsonResponse("Failed to retrieve User.", safe = False)
#     elif request.method == 'POST':
#         buyerUser_data=JSONParser().parse(request)
#         buyerUser_serializer = BuyerUserSerializer(data=buyerUser_data)
#         if buyerUser_serializer.is_valid():
#             buyerUser_serializer.save()
#             return JsonResponse("Added Successfully", safe = False)
#         return JsonResponse("Failed to Add.", safe = False)
#     elif request.method == 'PUT':
#         buyerUser_data = JSONParser().parse(request)
#         buyerUser = BuyerUser.objects.get(BuyerUserId = buyerUser_data['BuyerUserId'])
#         buyerUser_serializer = BuyerUserSerializer(buyerUser, data=buyerUser_data)
#         if buyerUser_serializer.is_valid():
#             buyerUser_serializer.save()
#             return JsonResponse("Updated Successfully!", safe = False)
#         return JsonResponse("Failed to Update.", safe = False)
#     elif request.method == 'DELETE':
#         try:
#             buyerUser = BuyerUser.objects.get(BuyerUserId = id)
#         except:
#             return JsonResponse("Failed to Delete.", safe = False)
#         buyerUser.delete()
#         return JsonResponse("Deleted Successfully!", safe = False)
    

# ### FILE SAVE ###
# @csrf_exempt
# def SaveFile(request):
#     try:
#         file = request.FILES['uploadedFile']
#         unique_filename = str(uuid.uuid4())
#         extension = str.split(file.name, '.')[1]
#         unique_filename += '.' + extension
#         file_name = default_storage.save(unique_filename, file)
#         return JsonResponse(data = response_helper(True, file_name), safe = False)
#     except:
#         return JsonResponse(data = response_helper(False, "Failed to Save File."), safe=False)

# ### DELETE FILE ###
# @csrf_exempt
# def DeleteFile(request):
#     if request.method != 'DELETE':
#         return JsonResponse(data = response_helper(False, "Invalid Request!"), safe = False)
#     try:
#         request_data = JSONParser().parse(request)
#         file_name = request_data['fileName']
#         if default_storage.exists(file_name):
#             default_storage.delete(file_name)
#             return JsonResponse(data = response_helper(True, "File Deleted Successfully!"), safe = False)
#         else:
#             return JsonResponse(data = response_helper(False, "No Such File"), safe = False)
#     except:
#         return JsonResponse(data = response_helper(False, "Failed to Delete File."), safe=False)
    

# ### GET ALL MESSAGES ###
# @csrf_exempt
# def DeleteFile(request):
#     if request.method != 'DELETE':
#         return JsonResponse("Invalid Request!", safe = False)
#     try:
#         request_data = JSONParser().parse(request)
#         file_name = request_data['fileName']
#         if default_storage.exists(file_name):
#             default_storage.delete(file_name)
#             return JsonResponse(data = response_helper(True, "File Deleted Successfully!"), safe = False)
#         else:
#             return JsonResponse(data = response_helper(False, "No Such File."), safe = False)
#     except:
#         return JsonResponse(data = response_helper(False, "Failed to Delete File."), safe=False)