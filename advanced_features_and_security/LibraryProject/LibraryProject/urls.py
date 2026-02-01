from django.contrib import admin
from django.urls import path, include  # include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookshelf.urls')),  # point to the app's urls.py
]
