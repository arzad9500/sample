from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user
from django.contrib.auth import authenticate
from .serializers  import *

#  have doubt check django 22 video
class userview(APIView):
    def post (self, request):
    
        # Check duplicate username
        if user.objects.filter(username=request.data['username']).exists():
            return Response({"error": "Username already exists"}, status=400)

        new_user = user(
            username=request.data['username'], # down --> .get(key, default_value)  --> If the key does not exist → use False
            is_superuser=request.data.get('is_superuser', False), # If the frontend sends "is_superuser": true → use that value , else false
            is_staff=True # Because if you create a user with: is_superuser=True , but is_staff=False --> Then Django admin will NOT allow login.
        )   # Django’s rule: Superusers MUST have is_staff=True


        new_user.set_password(request.data['password'])  # correct
        new_user.save()                                   # correct
        return Response({"message": "User created successfully"})

    
class user_login_view (APIView): # this for validate (check username and password)

    def post(self, request):
        #     user_verify = authenticate(
        #         username=request.data['username'], 
        #         password=request.data['password']
        #     )
        #     # print(user_verify) # this line make sence then make down logic ,  can access--> print(user_verify.date_joined)

        #     if user_verify is None: # matching data not found
        #         return Response('check your username or password')
        #     else:
        #         return Response('valid user')


        user_data = custom_token_serializer(data = request.data)
        if user_data.is_valid():
            return Response(user_data.validated_data)
        else:
            return Response(user_data.errors)