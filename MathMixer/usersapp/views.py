from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Organization
from .serializers import RegisterSerializer, LoginSerializer, OrganizationRegisterSerializer
from rest_framework.exceptions import ValidationError

# Регистрация
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Генерация токенов сразу после успешной регистрации
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({
                "message": "Пользователь успешно зарегистрирован.",
                "token": tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Логин
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Получаем данные из validated_data
            identifier = serializer.validated_data['username_or_nameorganization']
            password = serializer.validated_data['password']

            # Пробуем аутентифицировать пользователя
            user = authenticate(username=identifier, password=password)
            if user:
                tokens = serializer.get_tokens(user)
                return Response({"token": tokens}, status=status.HTTP_200_OK)

            # Пробуем найти организацию, если пользователь не найден
            try:
                organization = Organization.objects.get(nameorganization=identifier)
                if not organization.check_password(password):
                    raise ValidationError("Неверные учетные данные.")
                return Response(serializer.get_tokens(organization), status=status.HTTP_200_OK)
            except Organization.DoesNotExist:
                return Response({"message": "Неверные данные."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrganizationRegisterSerializer(data=request.data)
        if serializer.is_valid():
            organization = serializer.save()
            refresh = RefreshToken.for_user(organization)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({
                "message": "Организация успешно зарегистрирована.",
                "token": tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)