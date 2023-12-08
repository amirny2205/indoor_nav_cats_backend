from .models import CatModel
from .serializers import CatSerializer
from rest_framework import generics


class CatListCreate(generics.ListCreateAPIView):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer
