from django.urls import path,include

urlpatterns = [
    path('website/apis/',include('user.website.urls')),
]