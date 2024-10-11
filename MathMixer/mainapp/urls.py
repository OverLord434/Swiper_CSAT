from django.urls import path
from . import views
from .views import ProductSearchView, ProductDetailView

urlpatterns = [
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/characteristics/<int:category_id>/', views.get_characteristics, name='get_characteristics'),
    path('api/products/', views.add_product, name='add_product'),
    path('api/products/search/', ProductSearchView.as_view(), name='product-search'),
    path('api/products/<int:id_product>/', ProductDetailView.as_view(), name='product-detail'),
]