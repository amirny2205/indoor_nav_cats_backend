from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response


class UserCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, validated_data):
        d = validated_data.data
        u = User.objects.create(username=d['username'])
        u.set_password(d['password'])
        u.save()
        headers = self.get_success_headers(validated_data.data)
        return Response(validated_data.data, status=status.HTTP_201_CREATED, headers=headers)

