from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from .models import Profile
from rest_framework.validators import UniqueValidator
# Сериализатор для регистрации
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        error_messages={
            'required': _('Это поле обязательно.'),
            'invalid': _('Введите правильный адрес электронной почты.')
        }
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'error_messages': {
                    'required': _('Это поле обязательно.'),
                    'min_length': _('Пароль слишком короткий. Он должен содержать не менее 8 символов.'),
                    'common': _('Пароль слишком распространён.'),
                    'numeric': _('Пароль не может состоять только из цифр.')
                }
            }
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует."})

        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Этот адрес электронной почты уже используется.'))
        return value

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
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Неверные учетные данные.")
        else:
            raise serializers.ValidationError("Необходимо указать email, и пароль.")

        return data


    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined']

class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class ProfileSerializerImage(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['username', 'profile_picture']

    def update(self, instance, validated_data):
        # Обновляем данные профиля
        user_data = validated_data.pop('user', {})
        instance.user.username = user_data.get('username', instance.user.username)

        # Обновляем аватар, если он предоставлен
        profile_picture = validated_data.get('profile_picture', None)
        if profile_picture:
            instance.profile_picture = profile_picture

        instance.user.save()
        instance.save()
        return instance