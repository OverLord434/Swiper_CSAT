from django.contrib import admin
from .models import Product, Service, Category, Charackterstick, CategoryService, CharackterstickService

admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Charackterstick)
admin.site.register(CategoryService)
admin.site.register(CharackterstickService)

