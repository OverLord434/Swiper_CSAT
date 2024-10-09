from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, ProfileView

urlpatterns = [
    path('register/users', RegisterView.as_view(), name='register'),
    path('enter/user', LoginView.as_view(), name='login'),
    path('appheader/user', UserDetailView.as_view()),
    path('profile/date', ProfileView.as_view()),
]