from rest_framework import status,views
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from core.utils import normalize_email
from .serializers import WebsiteUserModelSerializer

"""
{
    "email":"test@user.com",
    "password":"Hello@123"
}
"""
class WebsiteUserLoginAPIView(views.APIView):
    def post(self,request):
        try:
            email= normalize_email(request.data['email'])
            user=authenticate(request,username=email,password=request.data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                data={
                    "refresh":str(refresh),
                    "access":str(refresh.access_token),
                    "user":WebsiteUserModelSerializer(user).data
                }
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid email or password"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : f"Something went wrong: {e}"}, status=status.HTTP_400_BAD_REQUEST)
