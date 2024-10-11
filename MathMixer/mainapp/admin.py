from django.contrib import admin
from .models import Product, Category, Charackterstick, Service, CategoryService, CharackterstickService

# Регистрация моделей в админке
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Charackterstick)
admin.site.register(Service)
admin.site.register(CategoryService)
admin.site.register(CharackterstickService)




