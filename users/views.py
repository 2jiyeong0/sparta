from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .jwt_claim_serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .jwt_claim_serializer import CustomTokenObtainPairSerializer
from .serializers import UserSerializer
from .models import User

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messeage":"회원 가입이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"messeage":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer