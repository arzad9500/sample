from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from liberary.models import *
from .serializers import *

# whatever we want import and use
generics.CreateAPIView # only post                 # Create a new object	POST
generics.ListAPIView # get all                     #	Get all objects	GET 
generics.RetrieveAPIView # get by id               # Get a single object	GET
generics.UpdateAPIView # update by  id             #  Update an object	PUT, PATCH
generics.DestroyAPIView # delete by id             # Delete an object	DELETE
generics.ListCreateAPIView # get all and post a new data     #	List all & Create new	GET, POST
generics.RetrieveDestroyAPIView # get by id and delete by id
generics.RetrieveUpdateAPIView # get by id and update by id
generics.RetrieveUpdateDestroyAPIView # id base get,update,delete  # View, Edit, Delete one object	GET, PUT, PATCH, DELETE

# this modelviewset so need router.py
class BookView(ModelViewSet):  # all method work here  (get , put , post , delete )

    queryset  =  Book.objects.all()
    serializer_class =  Book_serializer
    # here response is automatic
# this method is used for just store and take data use this is simple and goood

# ModelViewSet is no customable
#  apiview is fully customable
# generics is little customizable
class laptopView(generics.ListCreateAPIView): # generics is little customizable

    def get_queryset(self):
        return laptop.objects.filter(brand = 'dell') # filter based on condition

    queryset = laptop.objects.all()
    serializer_class = laptop_serilizers

    def perform_create(self, serializer):
        # print(self.request.data)
        serializer.save(user_type = "high performance") #  user_type field we use null= true , but we can handle here , check this models

class laptopViewById(generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        serializer.save(user_type = "low performance")

    queryset = laptop.objects.all()
    serializer_class = laptop_serilizers



