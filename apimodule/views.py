from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Hunde
from .serializers import HundeSerializer


class CreateDogs(APIView):  # Corrected class name to follow Python naming conventions
    def post(self, request, *args, **kwargs):
        serializer = HundeSerializer(data=request.data, many=True)
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

class ListCreat(generics.ListCreateAPIView):
    queryset = Hunde.objects.all()
    serializer_class = HundeSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DoggetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hunde.objects.all()
    serializer_class = HundeSerializer



