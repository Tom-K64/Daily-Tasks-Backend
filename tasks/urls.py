from django.urls import path,include

urlpatterns = [
    path('website/apis/',include('tasks.website.urls')),
]