from django.urls import include, path
from .views import ProductSearchView

urlpatterns = [
    path('api/product/cards', ProductSearchView.as_view()),
]