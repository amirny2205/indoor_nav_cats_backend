from django.urls import path
from .views import UserList, MessageList

urlpatterns = [
    path('userlist/', UserList.as_view()),
    path('messagelist/', MessageList.as_view())
]
