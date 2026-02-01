from django.urls import path
from . import views
from views import LibraryDetailView
from .views import list_books


urlpatterns = [
    path("", views.index, name="index"),
    path("books_list/", views.list_books, name="books_list"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication URLs
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
