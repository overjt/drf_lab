from django.shortcuts import render
from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer
####
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

# ViewSets define the view behavior.
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class Mascotas(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = PetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)