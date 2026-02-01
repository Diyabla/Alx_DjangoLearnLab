from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show in list view
    list_filter = ('publication_year', 'author')             # filter sidebar
    search_fields = ('title', 'author')                      # search box



# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)