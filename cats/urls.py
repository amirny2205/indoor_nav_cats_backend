from django.urls import path
from .views import CatDetail, CatListCreate

urlpatterns = [
    path('listcreate/', CatListCreate.as_view()),
    path('detail/<int:pk>/', CatDetail.as_view() )
]
