from .models import CatModel
from .serializers import CatSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CatListCreate(generics.ListCreateAPIView):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer

    def create(self, validated_data):
        if validated_data.user.is_anonymous:
            return Response("anonymous user is not allowed for cats creation", status=status.HTTP_400_BAD_REQUEST)
        else:
            validated_data.data["owner"] = validated_data.user.pk
            serializer = self.get_serializer(data=validated_data.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            
 

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatModel.objects.all()
    serializer_class = CatSerializer
