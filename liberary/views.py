from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from liberary.models import *
from .serializers import *

# whatever we want import and use
generics.CreateAPIView # only post                 # Create a new object	POST
generics.ListAPIView # get all                     #	Get all objects	GET 
generics.RetrieveAPIView # get by id               # Get a single object	GET
generics.UpdateAPIView # update by pass id         #  Update an object	PUT, PATCH
generics.DestroyAPIView # delete by it             # Delete an object	DELETE
generics.ListCreateAPIView # get all and post a new data     #	List all & Create new	GET, POST
generics.RetrieveDestroyAPIView # get by id and delete by id
generics.RetrieveUpdateAPIView # get by id and delete by id
generics.RetrieveUpdateDestroyAPIView # id base get,update,delete  # View, Edit, Delete one object	GET, PUT, PATCH, DELETE


class BookView(ModelViewSet):

    queryset  =  Book.objects.all()
    serializer_class =  Book_serializer


class laptopView(generics.ListCreateAPIView):

    def get_queryset(self):
        return laptop.objects.filter(brand = 'dell')

    queryset = laptop.objects.all()
    serializer_class = laptop_serilizers

    def perform_create(self, serializer):
        # print(self.request.data)
        serializer.save(user_type = "high performance")

class laptopViewById(generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        serializer.save(user_type = "low performance")

    queryset = laptop.objects.all()
    serializer_class = laptop_serilizers



