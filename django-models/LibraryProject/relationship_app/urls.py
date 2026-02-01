# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books_list/", views.list_books, name="books_list"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path('add_book/', views.add_book, name='add_book'),

    # URL for editing a book; <int:pk> is required for identifying the book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # URL for deleting a book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Optional: URL for listing books
    path('books_list/', views.list_books, name='books_list'),

    # Authentication URLs using class-based views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),  # Registration still function-based

    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
