# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hunde
from .serializers import HundeSerializer
from rest_framework import serializers

class CreateDogs(APIView):  # Corrected class name to follow Python naming conventions
    def post(self, request):
        serializer = HundeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DogList(APIView):  # Inherited from APIView
    def get(self, request):
        hunde = Hunde.objects.all()
        serializer = HundeSerializer(hunde, many=True)
        return Response(serializer.data)

class DeleteDogs(APIView):
    def delete(self, request, pk):
        hunde = Hunde.objects.get(pk=pk)
        hunde.delete()
        return Response('Item deleted')
    
class UpdateDogs(APIView):
    def put(self, request, pk):
        hunde = Hunde.objects.get(pk=pk)
        serializer = HundeSerializer(hunde, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)