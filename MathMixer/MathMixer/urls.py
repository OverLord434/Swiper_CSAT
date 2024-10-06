from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('auth/', include('usersapp.urls')),  # Подключение приложения авторизации
]