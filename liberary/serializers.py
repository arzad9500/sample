from rest_framework.serializers import ModelSerializer
from liberary.models import Book, laptop

class Book_serializer(ModelSerializer):

    class Meta :

        model = Book
        fields ='__all__'

class laptop_serilizers(ModelSerializer):

    class Meta:

        model = laptop
        fields ='__all__'