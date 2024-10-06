from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Organization


# Сериализатор для регистрации
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Сериализатор для входа (логина)
class LoginSerializer(serializers.Serializer):
    username_or_nameorganization = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        identifier = data.get("username_or_nameorganization")
        password = data.get("password")

        if identifier and password:
            user = authenticate(username=identifier, password=password)
            if not user:
                # Пробуем найти организацию
                try:
                    organization = Organization.objects.get(nameorganization=identifier)
                    if not organization.check_password(password):
                        raise serializers.ValidationError("Неверные учетные данные.")
                    return organization
                except Organization.DoesNotExist:
                    raise serializers.ValidationError("Неверные учетные данные.")
        else:
            raise serializers.ValidationError("Необходимо указать имя пользователя/организации и пароль.")
        return data

    def get_tokens(self, user_or_org):
        refresh = RefreshToken.for_user(user_or_org)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class OrganizationRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Organization
        fields = ('nameorganization', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        organization = Organization.objects.create_organization(
            nameorganization=validated_data['nameorganization'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return organization


