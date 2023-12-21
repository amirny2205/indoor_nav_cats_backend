from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, MessageSerializer
from .models import MessageModel

User = get_user_model()


class UserList(mixins.ListModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MessageList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
