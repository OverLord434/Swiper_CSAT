from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('nameorganization', 'email')
    search_fields = ('nameorganization', 'email')

admin.site.register(Organization, OrganizationAdmin)  # Регистрация Organization