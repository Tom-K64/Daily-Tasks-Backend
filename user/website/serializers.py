from rest_framework import serializers
from django.contrib.auth import get_user_model

class WebsiteUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name','is_superuser')