from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add custom fields to admin
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)
