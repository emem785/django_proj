from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import  Http404

# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ModifyUser(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(phone=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,fomat=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
            


