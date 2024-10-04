from django.urls import path
from .views import WebsiteUserLoginAPIView

urlpatterns = [
    path('login/',WebsiteUserLoginAPIView.as_view(),name="WebsiteUserLoginAPIView"),
]