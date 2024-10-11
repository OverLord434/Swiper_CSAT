from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/users', RegisterView.as_view(), name='register'),
    path('enter/user', LoginView.as_view(), name='login'),
    path('appheader/user', UserDetailView.as_view()),
    path('profile/date', ProfileView.as_view()),
    path('user/update', UserUpdateView.as_view()),
    path('profile/update', ProfileUpdateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)