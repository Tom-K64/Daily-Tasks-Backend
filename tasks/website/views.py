from rest_framework import generics,status,permissions,filters
from rest_framework.response import Response
from .serializers import WebsiteTaskModelSerializer
from ..models import TaskModel
from django_filters.rest_framework import DjangoFilterBackend


class WebsiteTaskModelListAPIView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = WebsiteTaskModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date',]
    ordering_fields = ['order',]

class WebsiteTaskModelCreateAPIView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = WebsiteTaskModelSerializer
    permission_classes = [permissions.IsAdminUser]

class WebsiteTaskModelGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = WebsiteTaskModelSerializer
    permission_classes = [permissions.IsAdminUser]