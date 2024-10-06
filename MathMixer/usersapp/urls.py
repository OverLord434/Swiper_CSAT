from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/users', RegisterView.as_view(), name='register'),
    path('enter/user', LoginView.as_view(), name='login'),
]