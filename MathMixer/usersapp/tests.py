from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class RegisterViewTest(APITestCase):

    def setUp(self):
        # Здесь можно добавить настройки, например, создание тестовых данных
        pass

    def test_registration_success(self):
        # Данные для регистрации пользователя
        url = reverse('register')  # Убедитесь, что этот URL соответствует вашему маршруту для регистрации
        data = {
            'username': 'newuser',
            'password': 'TestPassword123',
            'password2': 'TestPassword123',
            'email': 'newuser@example.com'
        }

        # Отправляем POST запрос на регистрацию
        response = self.client.post(url, data, format='json')

        # Проверяем, что запрос успешен и возвращает статус 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Пользователь успешно зарегистрирован.')

        # Проверяем, что пользователь действительно создан
        user = User.objects.get(username='newuser')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'newuser@example.com')

    def test_registration_failure(self):
        # Пробуем отправить некорректные данные
        url = reverse('register')
        data = {
            'username': '',  # Пустое имя пользователя, что является ошибкой
            'password': 'TestPassword123',
            'password2': 'T12',
            'email': 'invalidemail'  # Некорректный email
        }

        response = self.client.post(url, data, format='json')

        # Проверяем, что запрос вернет ошибку валидации
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)  # Убедимся, что ошибка для поля username
        self.assertIn('email', response.data)  # И для поля email

