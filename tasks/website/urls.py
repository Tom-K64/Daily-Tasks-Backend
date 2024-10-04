from django.urls import path
from .views import WebsiteTaskModelListAPIView,WebsiteTaskModelCreateAPIView,WebsiteTaskModelGenericAPIView

urlpatterns = [
    path('task-list-api/',WebsiteTaskModelListAPIView.as_view(),name="WebsiteTaskModelListAPIView"),
    path('task-create-api/',WebsiteTaskModelCreateAPIView.as_view(),name="WebsiteTaskModelCreateAPIView"),
    path('task-generic-api/<int:pk>/',WebsiteTaskModelGenericAPIView.as_view(),name="WebsiteTaskModelGenericAPIView"),
]
